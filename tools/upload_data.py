'''
Uploads a CSV file to the main data store.

This tool takes one command line argument, a filepath. To run it, try
something like this:
    `python -m tools.upload_data <YOUR_FILEPATH_HERE>`
'''
from urllib import parse, request
import pandas as pd
import sys

import requests

from app.model.review import Review


def main():
    command_line_args = sys.argv[1:]
    file_name = "tests/test_data.csv"
    if len(command_line_args) == 1:
        file_name = command_line_args[0]

    print("Uploading from file: " + file_name)
    filepath = None
    with open(file_name, 'rb') as f:
        file_response = requests.post("http://localhost:5002/file", files={"file": f})
        print("Status: " + str(file_response.status_code))
        file_data = file_response.json()
        filepath = file_data["data"]

    if filepath is not None:
        ingestion_query_parameters = parse.urlencode({"filepath": filepath})
        ingestion_request_url = "http://localhost:5002/batch?" + ingestion_query_parameters
        ingestion_request = request.Request(
            ingestion_request_url, method="PUT")
        ingestion_response = request.urlopen(ingestion_request)
        print("Status: " + str(ingestion_response.status))
    else:
        print("Error uploading file.")
    print("Done")


if __name__ == "__main__":
    main()
