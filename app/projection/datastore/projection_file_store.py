import io
import json
import logging
from minio import Minio


class ProjectionFileStore:
    '''
    This class uses MinIO to provide S3-like file storage to our
    projection datastore layer.
    '''

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

    def put_object(self, name: str, data: object):
        serialized_data = json.dumps(data).encode()
        self.client.put_object(bucket_name=self.bucket_name,
                               object_name=name,
                               length=len(serialized_data),
                               data=io.BytesIO(serialized_data))

    def check_if_object_exists(self, name: str):
        try:
            _ = self.client.stat_object(bucket_name=self.bucket_name,
                                       object_name=name)
            return True
        except:
            logging.warning("Object not found: " + name)
            return False

    def get_object(self, name: str):
        return json.loads(self.client.get_object(bucket_name=self.bucket_name,
                                                 object_name=name).data.decode())

