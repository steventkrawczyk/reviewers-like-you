package reviewers

import (
	"context"

	reviewers "github.com/steventkrawczyk/reviewers-like-you/app/common/go/resources"
	"github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"
)

type MainDatastoreServer struct {
	proto.UnimplementedMainDatastoreServiceServer
	DynamodbClient *reviewers.MainDatastore
	authors        []string
	cacheValid     bool
	// TODO we need a "new" function to set default values...
}

func (server *MainDatastoreServer) checkCache(review *proto.Review) bool {
	for _, author := range server.authors {
		if *review.Author == author {
			return true
		}
	}
	return false
}

func (server *MainDatastoreServer) restoreCache(review *proto.Review) {
	server.authors = append(server.authors, *review.Author)
	server.cacheValid = true
}

func (server *MainDatastoreServer) UploadReview(ctx context.Context, request *proto.UploadReviewRequest) (*proto.Payload, error) {
	var review *proto.Review
	review = request.GetReview()
	server.DynamodbClient.Upload(review)

	if !server.checkCache(review) {
		server.restoreCache(review)
	}

	message := ""
	category := ""
	status := int32(200)
	return &proto.Payload{Message: &message, Category: &category, Status: &status}, nil
}

func (server *MainDatastoreServer) BatchUploadReview(ctx context.Context, request *proto.BatchUploadReviewRequest) (*proto.Payload, error) {
	server.cacheValid = false
	server.DynamodbClient.BatchUpload(request.GetReviewList())

	message := ""
	category := ""
	status := int32(200)
	return &proto.Payload{Message: &message, Category: &category, Status: &status}, nil
}

func (server *MainDatastoreServer) GetReviewsByAuthor(ctx context.Context, request *proto.GetReviewsByAuthorRequest) (*proto.GetReviewsByAuthorResponse, error) {
	reviewList := proto.ReviewList{}
	server.DynamodbClient.Get(request.GetAuthor(), &reviewList)
	return &proto.GetReviewsByAuthorResponse{ReviewList: &reviewList}, nil
}

func (server *MainDatastoreServer) GetAuthors(ctx context.Context, request *proto.GetAuthorsRequest) (*proto.GetAuthorsResponse, error) {
	if server.cacheValid {
		return &proto.GetAuthorsResponse{Author: server.authors}, nil
	} else {
		authors := server.DynamodbClient.GetKeys()
		server.authors = authors
		server.cacheValid = true
		return &proto.GetAuthorsResponse{Author: authors}, nil
	}
}
