package reviewers

import (
	"context"

	"github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
	"github.com/steventkrawczyk/reviewers-like-you/app/common/go/resources"
)

type FilestoreServer struct {
	proto.UnimplementedFilestoreServiceServer
	MinioClient *reviewers.Filestore
}

func (server *FilestoreServer) UploadObject(ctx context.Context, request *proto.UploadObjectRequest) (*proto.Payload, error) {
	bucketName := request.GetBucketName()
	objectName := request.GetBucketName()
	serializedObject := request.GetBucketName()
	server.MinioClient.PutObject(bucketName, objectName, serializedObject)

	message := ""
	category := ""
	status := int32(200)
	return &proto.Payload{Message: &message, Category: &category, Status: &status}, nil
}

func (server *FilestoreServer) DownloadObject(ctx context.Context, request *proto.DownloadObjectRequest) (*proto.Payload, error) {
	bucketName := request.GetBucketName()
	objectName := request.GetBucketName()
	serializedObject := server.MinioClient.GetObject(bucketName, objectName)

	message := ""
	category := ""
	status := int32(200)
	return &proto.Payload{Message: &message, Category: &category, Status: &status, Data: &serializedObject}, nil
}
