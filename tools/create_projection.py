'''
Create a projection out of the data stored in the main data store. The
projection is stored in the projection data store.

This tool doesn't take any command line args. To run it, try something
like this:
    `python -m tools.create_projection`
'''
import logging
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine_factory import ProjectionEngineFactory


def main():
    logging.info("Initializing...")
    database = MainDatastoreFactory().build()
    projection_databse = ProjectionDatastoreFactory().build()
    projection_engine = ProjectionEngineFactory(
        database, projection_databse).build()
    logging.info("Creating projection...")
    projection_engine.create_projection()
    logging.info("Done.")


if __name__ == "__main__":
    main()
