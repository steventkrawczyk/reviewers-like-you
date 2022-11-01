package reviewers

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"

	"github.com/steventkrawczyk/reviewers-like-you/app/generated/go/proto"

	"log"
)

type Datastorer interface {
	Init(string, string)
	Upload(*proto.Review)
	BatchUpload(*proto.ReviewList)
	Get(string, *proto.ReviewList)
	GetKeys() []string
	CreateTable(string) string
	DeleteTable(string) string
	CheckHealth() bool
}

type MainDatastore struct {
	ddbSession  *session.Session
	ddbClient   *dynamodb.DynamoDB
	tableName   string
	initialized bool
}

func (this *MainDatastore) Init(endpoint string, tableName string) {
	this.ddbSession = session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable,
	}))
	this.ddbClient = dynamodb.New(this.ddbSession, aws.NewConfig().WithEndpoint(endpoint))
	this.tableName = tableName
	this.initialized = true
}

func (this *MainDatastore) serializeReview(review *proto.Review) map[string]*dynamodb.AttributeValue {
	var serializedReview map[string]*dynamodb.AttributeValue

	authorVal := dynamodb.AttributeValue{}
	authorVal.SetS(*review.Author)
	serializedReview["author"] = &authorVal

	movieVal := dynamodb.AttributeValue{}
	movieVal.SetS(*review.Movie)
	serializedReview["movie"] = &movieVal

	ratingVal := dynamodb.AttributeValue{}
	ratingVal.SetN(fmt.Sprintf("%f", *review.Rating))
	serializedReview["rating"] = &ratingVal

	return serializedReview
}

func (this *MainDatastore) Upload(review *proto.Review) {
	serializedReview := this.serializeReview(review)
	input := &dynamodb.PutItemInput{
		Item:      serializedReview,
		TableName: aws.String(this.tableName),
	}

	_, err := this.ddbClient.PutItem(input)
	if err != nil {
		log.Fatalf("Got error calling PutItem: %s", err)
	}
}

func (this *MainDatastore) BatchUpload(reviews *proto.ReviewList) {
	requestMap := make(map[string][]*dynamodb.WriteRequest)
	requestMap[this.tableName] = make([]*dynamodb.WriteRequest, 0)

	for _, review := range reviews.GetReview() {
		serializedReview := this.serializeReview(review)
		putRequest := &dynamodb.PutRequest{Item: serializedReview}
		writeRequest := &dynamodb.WriteRequest{PutRequest: putRequest}
		requestMap[this.tableName] = append(requestMap[this.tableName], writeRequest)
	}

	batchRequest := &dynamodb.BatchWriteItemInput{RequestItems: requestMap}

	_, err := this.ddbClient.BatchWriteItem(batchRequest)
	if err != nil {
		log.Fatalf("Got error calling BatchWriteItem: %s", err)
	}
}

func (this *MainDatastore) getPage(author string, keyConditionExpression string, lastEvaluatedKey map[string]*dynamodb.AttributeValue, reviewList *proto.ReviewList) map[string]*dynamodb.AttributeValue {
	input := &dynamodb.QueryInput{
		TableName:              aws.String(this.tableName),
		KeyConditionExpression: aws.String(keyConditionExpression),
		ExclusiveStartKey:      lastEvaluatedKey,
	}

	results, err := this.ddbClient.Query(input)
	if err != nil {
		log.Fatalf("Got error calling Query: %s", err)
	}

	for _, item := range results.Items {
		var rating32 float32
		rating, err := strconv.ParseFloat(*item["rating"].N, 32)
		rating32 = float32(rating)
		if err != nil {
			log.Fatalf("Got error deserializing float: %s", err)
		}
		review := proto.Review{}
		review.Author = item["author"].S
		review.Movie = item["movie"].S
		review.Rating = &rating32
		reviewList.Review = append(reviewList.Review, &review)
	}

	return results.LastEvaluatedKey
}

func (this *MainDatastore) Get(author string, reviewList *proto.ReviewList) {
	keyConditionExpression := "author = :" + author

	lastEvaluatedKey := this.getPage(author, keyConditionExpression, make(map[string]*dynamodb.AttributeValue), reviewList)
	for len(lastEvaluatedKey) > 0 {
		lastEvaluatedKey = this.getPage(author, keyConditionExpression, lastEvaluatedKey, reviewList)
	}
}

func (this *MainDatastore) scanPage(projectionExpression string, authors []string, lastEvaluatedKey map[string]*dynamodb.AttributeValue) map[string]*dynamodb.AttributeValue {
	input := &dynamodb.ScanInput{
		TableName:            aws.String(this.tableName),
		ProjectionExpression: aws.String(projectionExpression),
		ExclusiveStartKey:    lastEvaluatedKey,
	}

	results, err := this.ddbClient.Scan(input)
	if err != nil {
		log.Fatalf("Got error calling Scan: %s", err)
	}

	for _, item := range results.Items {
		author := *item["author"].S
		authors = append(authors, author)
	}

	return results.LastEvaluatedKey
}

func (this *MainDatastore) GetKeys() []string {
	projectionExpression := "author"
	authors := []string{}
	lastEvaluatedKey := this.scanPage(projectionExpression, authors, make(map[string]*dynamodb.AttributeValue))
	for len(lastEvaluatedKey) > 0 {
		lastEvaluatedKey = this.scanPage(projectionExpression, authors, lastEvaluatedKey)
	}

	return authors
}

func (this *MainDatastore) CreateTable(tableName string) string {
	input := &dynamodb.CreateTableInput{
		AttributeDefinitions: []*dynamodb.AttributeDefinition{
			{
				AttributeName: aws.String("author"),
				AttributeType: aws.String("S"),
			},
			{
				AttributeName: aws.String("rating"),
				AttributeType: aws.String("N"),
			},
			{
				AttributeName: aws.String("movie"),
				AttributeType: aws.String("S"),
			},
		},
		GlobalSecondaryIndexes: []*dynamodb.GlobalSecondaryIndex{
			{
				IndexName: aws.String("movie-index"),
				Projection: &dynamodb.Projection{
					ProjectionType: aws.String("ALL"),
				},
				ProvisionedThroughput: &dynamodb.ProvisionedThroughput{
					ReadCapacityUnits:  aws.Int64(10),
					WriteCapacityUnits: aws.Int64(10),
				},
				KeySchema: []*dynamodb.KeySchemaElement{
					{
						AttributeName: aws.String("movie"),
						KeyType:       aws.String("HASH"),
					},
				},
			},
		},
		KeySchema: []*dynamodb.KeySchemaElement{
			{
				AttributeName: aws.String("author"),
				KeyType:       aws.String("HASH"),
			},
			{
				AttributeName: aws.String("rating"),
				KeyType:       aws.String("RANGE"),
			},
		},
		ProvisionedThroughput: &dynamodb.ProvisionedThroughput{
			ReadCapacityUnits:  aws.Int64(10),
			WriteCapacityUnits: aws.Int64(10),
		},
		TableName: aws.String(tableName),
	}

	response, err := this.ddbClient.CreateTable(input)
	if err != nil {
		if strings.Contains(err.Error(), "ResourceInUseException") {
			return "ALREADY_EXISTS"
		}
		log.Fatalf("Got error calling CreateTable: %s", err)
	}

	this.tableName = tableName
	return *response.TableDescription.TableStatus
}

func (this *MainDatastore) DeleteTable(tableName string) string {
	input := &dynamodb.DeleteTableInput{TableName: aws.String(tableName)}
	_, err := this.ddbClient.DeleteTable(input)
	if err != nil {
		log.Fatalf("Got error calling DeleteTable: %s", err)
	}

	return "DELETED"
}

func (this *MainDatastore) CheckHealth() bool {
	return this.initialized
}
