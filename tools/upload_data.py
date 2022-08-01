'''
Uploads a CSV file to the main data store.

This tool takes one command line argument, a filepath. To run it, try
something like this:
    `python -m tools.upload_data <YOUR_FILEPATH_HERE>`
'''
from urllib import parse, request
import pandas as pd
import sys

from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.ingestion.main_datastore_factory import MainDatastoreFactory


def main():
    command_line_args = sys.argv[1:]
    file_name = "tests/test_data.csv"
    if len(command_line_args) == 1:
        file_name = command_line_args[0]

    print("Uploading from file: " + file_name)
    ingestion_query_parameters = parse.urlencode({"filepath": file_name})
    ingestion_request_url = "http://localhost:5001/batch?" + ingestion_query_parameters
    ingestion_request = request.Request(ingestion_request_url, method="PUT")
    ingestion_response = request.urlopen(ingestion_request)
    print("Status: " + str(ingestion_response.status))


if __name__ == "__main__":
    main()
