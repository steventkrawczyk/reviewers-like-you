package reviewers

import (
	"context"

	reviewers "github.com/steventkrawczyk/reviewers-like-you/app/common/go/resources"
	"github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
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

func (server *FilestoreServer) DownloadObject(ctx context.Context, request *proto.DownloadObjectRequest) (*proto.DownloadObjectResponse, error) {
	bucketName := request.GetBucketName()
	objectName := request.GetBucketName()

	found := false
	serializedObject := ""
	if server.MinioClient.CheckIfObjectExists(bucketName, objectName) {
		found = true
		serializedObject = server.MinioClient.GetObject(bucketName, objectName)
	}

	return &proto.DownloadObjectResponse{Found: &found, Data: &serializedObject}, nil
}

func (server *FilestoreServer) StatObject(ctx context.Context, request *proto.StatObjectRequest) (*proto.StatObjectResponse, error) {
	bucketName := request.GetBucketName()
	objectName := request.GetBucketName()

	found := server.MinioClient.CheckIfObjectExists(bucketName, objectName)
	return &proto.StatObjectResponse{Found: &found}, nil
}
