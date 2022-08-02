from io import StringIO
import uuid

import pandas as pd
from app.ingestion.datastore.upload_file_store import UploadFileStore


class UploadClient:
    def __init__(self, upload_file_store: UploadFileStore):
        self.upload_file_store = upload_file_store

    def upload_file(self, data: bytes) -> str:
        name = str(uuid.uuid4()) + ".csv"
        self.upload_file_store.put_object(name, data)
        return name
    
    def upload_dataframe(self, data: pd.DataFrame) -> str:
        data_string = data.to_csv()
        name = uuid.uuid4() + ".csv"
        self.upload_file_store.put_object(name, str.encode(data_string))
        return name

    def download_dataframe(self, name) -> pd.DataFrame:
        data_string = self.upload_file_store.get_object(name).decode()
        data = pd.read_csv(StringIO(data_string))
        return data
        
        