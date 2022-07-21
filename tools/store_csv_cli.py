'''
The purpose of this CLI is to upload structured data, which has already
been cleaned before it was stored. The format of the data is the
following: (author, movie, review) where author and movie are strings
and review is a float from 0 to 1. To use this CLI, provide a file path
to a csv with data stored in this format, e.g.

python store_csv_cli.py /your/file/path.csv

NOTE: This is untested and under development.
'''
import pandas as pd
import sys

def main():
    # TODO: validate command line args and input data format
    file_name = sys.argv[1:]
    input_data = pd.read_csv(file_name, header=0)

    database = MainDatastoreProxy()
    client = DataframeIngestionClient(database)
    client.upload(input_data)

if __name__ == "__main__":
    main()