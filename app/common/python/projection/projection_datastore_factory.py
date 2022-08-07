from app.common.python.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy


class ProjectionDatastoreFactory:
    '''
    Factory class for ProjectionDatastoreProxy.
    '''

    def __init__(self):
        pass

    def build(self) -> ProjectionDatastoreProxy:
        return ProjectionDatastoreProxy()
