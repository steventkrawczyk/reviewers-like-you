

from app.ingestion.datastore.upload_client import UploadClient
from app.ingestion.datastore.upload_file_store import UploadFileStore


class UploadClientFactory:
    def __init__(self, endpoint_url, bucket_name):
        self.endpoint_url = endpoint_url
        self.bucket_name = bucket_name

    def build(self):
        upload_file_store = UploadFileStore(self.endpoint_url, self.bucket_name)
        upload_file_store.make_projections_bucket()
        upload_client = UploadClient(upload_file_store)
        return upload_client