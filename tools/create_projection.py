'''
Create a projection out of the data stored in the main data store. The
projection is stored in the projection data store.

This tool doesn't take any command line args. To run it, try something
like this:
    `python -m tools.create_projection`
'''
from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine import ProjectionEngine


def main():
    print("Initializing...")
    database = MainDatastoreProxy()
    projection_databse = ProjectionDatastoreFactory().build()
    projection_engine = ProjectionEngine(database, projection_databse)
    print("Creating projection...")
    projection_engine.create_projection()
    print("Done.")


if __name__ == "__main__":
    main()
