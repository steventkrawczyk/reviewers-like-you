import io
import json
import logging
from minio import Minio


class UploadFileStore:
    def __init__(self, endpoint_url: str, bucket_name: str):
        self.bucket_name = bucket_name
        # TODO Move these keys to env variables
        self.client = \
            Minio(endpoint_url, access_key="minioadmin",
                  secret_key="minioadmin", secure=False)

    # TODO setup versioning
    def make_projections_bucket(self):
        already_exists = self.client.bucket_exists(self.bucket_name)
        if not already_exists:
            self.client.make_bucket(self.bucket_name)

    def put_object(self, name: str, data: bytes):
        self.client.put_object(bucket_name=self.bucket_name,
                               object_name=name,
                               length=len(data),
                               data=io.BytesIO(data))

    def check_if_object_exists(self, name: str):
        try:
            _ = self.client.stat_object(bucket_name=self.bucket_name,
                                        object_name=name)
            return True
        except:
            logging.warning("Object not found: " + name)
            return False

    def get_object(self, name: str):
        return self.client.get_object(bucket_name=self.bucket_name, object_name=name).data
