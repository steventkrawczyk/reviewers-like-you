// APIs to interact with uploads bucket using kafka topic of recent files:
// Check upload bucket - make sure that first row of each file is in DDB table
// Clean upload bucket - delete files in upload bucket

// Kafka topic with user ratings, API to initiate forward to elasticsearch (might need new service, or use ingestion)

// Manage jobs like scraping and projection engine via control plane service

// Proxy for manual file upload (ideally all tools go through this service and cron jobs)
// Manage resources
// Health check and wait for 200 - fan out and target server

// Eventually API to trigger reloads for movies, match, similarity, or partition