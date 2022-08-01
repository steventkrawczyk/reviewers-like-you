'''
Create a projection out of the data stored in the main data store. The
projection is stored in the projection data store.

This tool doesn't take any command line args. To run it, try something
like this:
    `python -m tools.create_projection`
'''
from urllib import request


def main():
    print("Creating projection...")
    create_request_url = "http://localhost:5001/create"
    create_request = request.Request(create_request_url, method="PUT")
    create_response = request.urlopen(create_request)
    print("Status: " + str(create_response.status))


if __name__ == "__main__":
    main()
