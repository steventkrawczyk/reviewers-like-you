class DefaultConfig(dict):
    '''
    Configuration used when no file is provided.
    '''

    default_values: dict = {
        "dynamo_endpoint_url": "http://dynamodb-local:8000",
        "minio_endpoint_url": "minio:9000",
        "table_name": "movie_reviews",
        "projection_bucket_name": "projections",
        "projection_filepath_root": "data/projection_",
        "movie_indices_filepath": "data/movie_indices.json",
        "upload_bucket_name": "uploads",
        "in_memory": False,
        "reload_for_testing": True
    }

    def __getitem__(self, key):
        if key not in self.traits.keys():
            raise KeyError
        return self.default_values[key]
