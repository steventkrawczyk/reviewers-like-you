'''
Uploads a CSV file to the main data store.

This tool takes one command line argument, a filepath. To run it, try
something like this:
    `python -m tools.upload_csv <YOUR_FILEPATH_HERE>`
'''
import pandas as pd
import sys

from app.main_datastore.dataframe_ingestion_client import DataframeIngestionClient
from app.main_datastore.main_datastore_proxy import MainDatastoreProxy

def main():
    print("Initializing")
    database = MainDatastoreProxy()
    client = DataframeIngestionClient(database)
    file_name = sys.argv[1:][0]
    input_data = pd.read_csv(file_name, header=0)

    print("Uploading from file: " + file_name)
    client.upload(input_data)
    print("Done")

if __name__ == "__main__":
    main()
