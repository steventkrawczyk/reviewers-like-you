package reviewers

import (
	"context"
	"log"
	"net"
	"strings"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	"github.com/golang/protobuf/jsonpb"
	config "github.com/steventkrawczyk/reviewers-like-you/app/common/go/config"
	proto "github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
)

type IngestionServer struct {
	proto.UnimplementedIngestionServiceServer
	Client       proto.MainDatastoreServiceClient
	FileClient   proto.FilestoreServiceClient
	AdmninClient proto.DatastoreAdminServiceClient
	BucketName   string
}

func (server *IngestionServer) IngestReview(ctx context.Context, req *proto.IngestReviewRequest) (*proto.Payload, error) {
	review := req.Review
	payload, err := server.Client.UploadReview(ctx, &proto.UploadReviewRequest{Review: review})
	return payload, err
}

func (server *IngestionServer) IngestBatch(ctx context.Context, req *proto.IngestBatchRequest) (*proto.Payload, error) {
	bucketName := "ingestion"
	response, err := server.FileClient.DownloadObject(ctx, &proto.DownloadObjectRequest{BucketName: &bucketName, ObjectName: req.Filename})
	if err != nil {
		log.Fatalln(err)
	}

	var reviewList proto.ReviewList
	if response.GetFound() {
		stringObject := response.GetData()
		jsonpb.Unmarshal(strings.NewReader(stringObject), &reviewList)
	}

	reviewSlice := reviewList.GetReview()
	reviewIndex := 0
	for reviewIndex < len(reviewSlice) {
		batchList := proto.ReviewList{}
		batchIndex := 0
		// TODO Parameterize batch size
		for (batchIndex < 25) && (reviewIndex < len(reviewSlice)) {
			review := reviewSlice[reviewIndex]
			batchList.Review = append(batchList.Review, review)
			reviewIndex += 1
			batchIndex += 1
		}
		_, err = server.Client.BatchUploadReview(ctx, &proto.BatchUploadReviewRequest{ReviewList: &batchList})
		if err != nil {
			log.Fatalln(err)
		}
	}

	message := ""
	category := ""
	status := int32(200)
	return &proto.Payload{Message: &message, Category: &category, Status: &status}, nil
}

func (server *IngestionServer) CheckHealth(ctx context.Context, req *proto.HealthCheckRequest) (*proto.Payload, error) {
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

	client := proto.NewMainDatastoreServiceClient(conn)
	fileClient := proto.NewFilestoreServiceClient(conn)
	adminClient := proto.NewDatastoreAdminServiceClient(conn)

	listener, err := net.Listen("tcp", ":5000")
	if err != nil {
		log.Fatalln(err)
	}
	ingestionServer := grpc.NewServer()

	proto.RegisterIngestionServiceServer(ingestionServer, &IngestionServer{UnimplementedIngestionServiceServer: proto.UnimplementedIngestionServiceServer{},
		Client: client, FileClient: fileClient, AdmninClient: adminClient, BucketName: configuration.UploadBucketName})

	reflection.Register(ingestionServer)

	err = ingestionServer.Serve(listener)
	if err != nil {
		log.Fatalln(err)
	}
}
