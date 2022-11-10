from rest_framework.routers import SimpleRouter
from search_algorithm.viewsets import ShortestPathViewset

routes = SimpleRouter()

routes.register(r'shortest-path', ShortestPathViewset,
                basename='shortest-path')

urlpatterns = [
    *routes.urls
]
