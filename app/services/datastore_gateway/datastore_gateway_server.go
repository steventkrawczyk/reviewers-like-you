package reviewers

import (
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	resources "github.com/steventkrawczyk/reviewers-like-you/app/common/go/resources"
	config "github.com/steventkrawczyk/reviewers-like-you/app/common/go/config"
	proto "github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
)

func main() {
	var dynamodbClient resources.MainDatastore
	var minioClient resources.Filestore

	var configuration config.Configuration
	configuration.Load("app/config.yml")

	dynamodbClient = resources.MainDatastore{}
	minioClient = resources.Filestore{}

	dynamodbClient.Init(configuration.DynamoEndpointUrl, configuration.TableName)
	minioClient.Init(configuration.MinioEndpointUrl)

	listener, err := net.Listen("tcp", ":5000")
	if err != nil {
		log.Fatalln(err)
	}

	gatewayServer := grpc.NewServer()

	proto.RegisterMainDatastoreServiceServer(gatewayServer, &MainDatastoreServer{UnimplementedMainDatastoreServiceServer: proto.UnimplementedMainDatastoreServiceServer{}, DynamodbClient: &dynamodbClient})
	proto.RegisterFilestoreServiceServer(gatewayServer, &FilestoreServer{UnimplementedFilestoreServiceServer: proto.UnimplementedFilestoreServiceServer{}, MinioClient: &minioClient})
	proto.RegisterDatastoreAdminServiceServer(gatewayServer, &DatastoreAdminServer{UnimplementedDatastoreAdminServiceServer: proto.UnimplementedDatastoreAdminServiceServer{}, DynamodbClient: &dynamodbClient, MinioClient: &minioClient})

	reflection.Register(gatewayServer)	

	err = gatewayServer.Serve(listener)
	if err != nil {
		log.Fatalln(err)
	}
}
