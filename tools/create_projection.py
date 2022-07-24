'''
Create a projection out of the data stored in the main data store. The
projection is stored in the projection data store.

This tool doesn't take any command line args. To run it, try something
like this:
    `python -m tools.create_projection`
'''
from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy
from app.projection.projection_engine import ProjectionEngine


def main():
    database = MainDatastoreProxy()
    projection_databse = ProjectionDatastoreProxy()
    projection_engine = ProjectionEngine(database, projection_databse)
    projection_engine.create_projection()

if __name__ == "__main__":
    main()
