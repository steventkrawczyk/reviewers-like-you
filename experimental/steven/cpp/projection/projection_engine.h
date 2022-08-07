class ProjectionEngine {};

// class ProjectionEngine:
//     '''
//     This class is used to download data from the main datastore and create
//     a projection of popular movies to use for similarity computations.
//     '''

//     def __init__(self, main_datastore_proxy: MainDatastoreProxy,
//                  projection_datastore_proxy: ProjectionDatastoreProxy,
//                  popularity_analyzer: PopularityAnalyzer,
//                  projection_builder: ProjectionBuilder):
//         self.main_datastore_proxy = main_datastore_proxy
//         self.projection_datastore_proxy = projection_datastore_proxy
//         self.popularity_analyzer = popularity_analyzer
//         self.projection_builder = projection_builder

//     def create_projection(self) -> None:
//         authors = list(self.main_datastore_proxy.get_keys())
//         popular_movies = self.popularity_analyzer.compute_popular_movies(
//             authors)
//         author_vectors, movie_indices =
//         self.projection_builder.build_vectors(
//             popular_movies, authors)
//         self.projection_datastore_proxy.upload(author_vectors, movie_indices)

// class ProjectionEngineFactory:
//     '''
//     A factory class for ProjectionEngine.
//     '''
//     def __init__(self, main_datastore_proxy: MainDatastoreProxy,
//                  projection_datastore_proxy: ProjectionDatastoreProxy):
//         self.main_datastore_proxy = main_datastore_proxy
//         self.projection_datastore_proxy = projection_datastore_proxy

//     def build(self):
//         popularity_analyzer = PopularityAnalyzer(self.main_datastore_proxy)
//         projection_builder = ProjectionBuilder(self.main_datastore_proxy)
//         return ProjectionEngine(self.main_datastore_proxy,
//                                 self.projection_datastore_proxy,
//                                 popularity_analyzer, projection_builder)
