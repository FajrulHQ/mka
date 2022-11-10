from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from search_algorithm import search_algorithm
from search_algorithm.serializers import ShortestPathSerializer


class ShortestPathViewset(ModelViewSet):
    http_method_names = ['post']
    serializer_class = ShortestPathSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            city = serializer.validated_data['city']
            method = serializer.validated_data['method']
            path = search_algorithm(city, method)
            return Response(path, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
