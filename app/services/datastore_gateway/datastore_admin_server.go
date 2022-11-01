package reviewers

import (
	"context"

	"github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
	resources "github.com/steventkrawczyk/reviewers-like-you/app/services/datastore_gateway/resources"
)

// TODO add mutexes to resources to block for admin commands
type DatastoreAdminServer struct {
	proto.UnimplementedDatastoreAdminServiceServer
	DynamodbClient *resources.MainDatastore
	MinioClient    *resources.Filestore
}

func (server *DatastoreAdminServer) CheckHealth(ctx context.Context, request *proto.HealthCheckRequest) (*proto.Payload, error) {
	message := ""
	category := ""
	healthy := server.DynamodbClient.CheckHealth() && server.MinioClient.CheckHealth()
	if healthy {
		status := int32(200)
		return &proto.Payload{Message: &message, Category: &category, Status: &status}, nil
	} else {
		status := int32(500)
		return &proto.Payload{Message: &message, Category: &category, Status: &status}, nil
	}
}

func (server *DatastoreAdminServer) ManageResource(ctx context.Context, request *proto.ManageResourceRequest) (*proto.Payload, error) {
	var status string
	if request.Action == proto.Action_CREATE.Enum() {
		if request.Resource == proto.Resource_TABLE.Enum() {
			status = server.DynamodbClient.CreateTable(*request.Name)
		} else {
			if server.MinioClient.CheckIfBucketExists(*request.Name) {
				status = "ALREADY_EXISTS"
			} else {
				server.MinioClient.MakeBucket(*request.Name)
				status = "ACTIVE"
			}
		}
	} else {
		if request.Resource == proto.Resource_TABLE.Enum() {
			status = server.DynamodbClient.DeleteTable(*request.Name)
		} else {
			if server.MinioClient.CheckIfBucketExists(*request.Name) {
				status = "DOES_NOT_EXIST"
			} else {
				server.MinioClient.DeleteBucket(*request.Name)
				status = "DELETED"
			}
		}
	}

	message := ""
	category := ""
	statusCode := int32(200)
	return &proto.Payload{Message: &message, Category: &category, Status: &statusCode, Data: &status}, nil
}
