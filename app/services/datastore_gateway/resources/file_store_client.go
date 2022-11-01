package reviewers

import (
	"log"
	"strings"

	"github.com/minio/minio-go"
)

type Filestorer interface {
	Init(string)
	MakeBucket(string)
	DeleteBucket(string)
	PutObject(string, string, string)
	GetObject(string, string) string
	CheckIfObjectExists(string, string) bool
	CheckIfBucketExists(string) bool
	CheckHealth() bool
}

type Filestore struct {
	minioClient *minio.Client
	initialized bool
}

func (this Filestore) Init(endpoint string) {
	minioClient, err := minio.New(endpoint, "minioadmin", "minioadmin", false)
	if err != nil {
		log.Fatalln(err)
	}

	this.minioClient = minioClient
	this.initialized = true
}

func (this Filestore) MakeBucket(bucketName string) {
	err := this.minioClient.MakeBucket(bucketName, "")
	if err != nil {
		log.Fatalln(err)
	}
}

func (this Filestore) DeleteBucket(bucketName string) {
	err := this.minioClient.RemoveBucket(bucketName)
	if err != nil {
		log.Fatalln(err)
	}
}

func (this Filestore) PutObject(bucketName string, objectName string, serializedObject string) {
	reader := strings.NewReader(serializedObject)
	this.minioClient.PutObject(bucketName, objectName, reader, reader.Size(), minio.PutObjectOptions{})
}

func (this Filestore) GetObject(bucketName string, objectName string) string {
	object, err := this.minioClient.GetObject(bucketName, objectName, minio.GetObjectOptions{})
	if err != nil {
		log.Fatalln(err)
	}

	var objectBytes []byte
	object.Read(objectBytes)
	return string(objectBytes)
}

func (this Filestore) CheckIfObjectExists(bucketName string, objectName string) bool {
	_, err := this.minioClient.StatObject(bucketName, objectName, minio.StatObjectOptions{})
	if err != nil {
		log.Fatalln(err)
	}
	return err == nil
}

func (this Filestore) CheckIfBucketExists(bucketName string) bool {
	exists, err := this.minioClient.BucketExists(bucketName)
	if err != nil {
		log.Fatalln(err)
	}
	return exists
}

func (this Filestore) CheckHealth() bool {
	return this.initialized
}
