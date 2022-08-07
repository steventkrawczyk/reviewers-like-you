package reviewers

import (
	"io/ioutil"
	"log"

	"gopkg.in/yaml.v2"
)

type Configuration struct {
	DynamoEndpointUrl   string `yaml:"dynamo_endpoint_url"`
	MinioEndpointUrl    string `yaml:"minio_endpoint_url"`
	TableName           string `yaml:"table_name"`
	UploadBucketName    string `yaml:"upload_bucket_name"`
	DatastoreGatewayUrl string `yaml:"datastore_gateway_url"`
}

func (c *Configuration) Load(filepath string) *Configuration {
	yamlFile, err := ioutil.ReadFile(filepath)
	if err != nil {
		log.Printf("yamlFile.Get err   #%v ", err)
	}
	err = yaml.Unmarshal(yamlFile, c)
	if err != nil {
		log.Fatalf("Unmarshal: %v", err)
	}

	return c
}
