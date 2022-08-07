package reviewers

import (
	"bufio"
	"bytes"
	"context"
	"encoding/csv"
	"io"
	"log"
	"net"
	"strconv"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	"github.com/golang/protobuf/jsonpb"
	config "github.com/steventkrawczyk/reviewers-like-you/app/common/go/config"
	proto "github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
)

type UploadServer struct {
	proto.UnimplementedUploadServiceServer
	Client proto.FilestoreServiceClient
	AdmninClient proto.DatastoreAdminServiceClient
	BucketName string
}

func (server *UploadServer) readFile(fileBytes []byte) [][]string {
	r := bytes.NewReader(fileBytes)

	headers, err := bufio.NewReader(r).ReadSlice('\n')
    if err != nil {
        log.Fatalln(err)
    }
    _, err = r.Seek(int64(len(headers)), io.SeekStart)
    if err != nil {
        log.Fatalln(err)
    }

    csvReader := csv.NewReader(r)
    records, err := csvReader.ReadAll()
    if err != nil {
        log.Fatalln(err)
    }

    return records
}

func (server *UploadServer) createReviewList(reviews [][]string, outputList *proto.ReviewList) {
	// We assume our data is author,movie,rating
	for _, review := range reviews {
		author := review[0]
		movie := review[1]
		rating64, _ := strconv.ParseFloat(review[2], 32)
		rating := float32(rating64)

		reviewObject := proto.Review{Author: &author, Movie: &movie, Rating: &rating}
		outputList.Review = append(outputList.Review, &reviewObject)
	}
}
	

func (server *UploadServer) UploadFile(ctx context.Context, req *proto.UploadFileRequest) (*proto.Payload, error) {
	records := server.readFile(req.Body)
	var reviewList proto.ReviewList
	server.createReviewList(records, &reviewList)

	m := jsonpb.Marshaler{}
    js, err := m.MarshalToString(&reviewList)

	payload, err := server.Client.UploadObject(ctx, &proto.UploadObjectRequest{BucketName: &server.BucketName, ObjectName: req.Name, SerializedObject: &js})
	return payload, err
}

func (server *UploadServer) CheckHealth(ctx context.Context, req *proto.HealthCheckRequest) (*proto.Payload, error) {
	payload, err := server.AdmninClient.CheckHealth(ctx, &proto.HealthCheckRequest{})
	return payload, err
}

func main() {
	var configuration config.Configuration
	configuration.Load("app/config.yml")

	conn, err := grpc.Dial(configuration.DatastoreGatewayUrl)
	if err != nil {
		log.Fatalln(err)
	}

	client := proto.NewFilestoreServiceClient(conn)
	adminClient := proto.NewDatastoreAdminServiceClient(conn)

	listener, err := net.Listen("tcp", ":5000")
	if err != nil {
		log.Fatalln(err)
	}

	uploadServer := grpc.NewServer()

	proto.RegisterUploadServiceServer(uploadServer, &UploadServer{UnimplementedUploadServiceServer: proto.UnimplementedUploadServiceServer{}, 
		Client: client, AdmninClient: adminClient, BucketName: configuration.UploadBucketName})

	reflection.Register(uploadServer)	

	err = uploadServer.Serve(listener)
	if err != nil {
		log.Fatalln(err)
	}
}
