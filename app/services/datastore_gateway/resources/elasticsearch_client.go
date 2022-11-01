package reviewers

import (
	"github.com/elastic/go-elasticsearch"
)

type UserReview struct {
	version string
	ratings []float32
}

type Version struct {
	version       string
	movie_indices []string
}

type UserReviewStorer interface {
	Init(string, string)
	Upload(*UserReview)
	BatchUpload(*[]UserReview)
	GetByVersion(string) // TODO: paging
	CheckHealth() bool
}

type VersionDataStorer interface {
	Init(string, string)
	Upload(*Version)
	GetVersionData(string)
	CheckHealth() bool
}

type UserReviewDatastore struct {
	client      *elasticsearch.Client
	initialized bool
}
