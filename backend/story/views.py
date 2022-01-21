# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
# from article.serializers import ArticleDetailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from story.models import Slides, Vehicles, VehicleDetail, Stories
# from rest_framework.permissions import IsAdminUser
from story.permissions import IsAdminUserOrReadOnly
from story.serializers import SlidesSerializer, VehiclesSerializer, VehicleDetailSerializer, StoriesSerializer


# from article.serializers import ArticleListSerializer


class SlidesViewSet(viewsets.ModelViewSet):
    """故事视图集"""
    queryset = Slides.objects.all()
    serializer_class = SlidesSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['header']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_queryset(self):
    #     queryset = self.queryset
    #     username = self.request.query_params.get('username', None)
    #
    #     if username is not None:
    #         queryset = queryset.filter(author__username=username)
    #
    #     return queryset


class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer
    permission_classes = [IsAdminUserOrReadOnly]

# class VehiclesViewSet(APIView):
#     # queryset = Vehicles.objects.all()
#     serializer_class = VehiclesSerializer
#
#     def get(self, request, format=None):
#         vehicles_ = Vehicles.objects.all()
#         vehicles_ = [model_to_dict(item) for item in vehicles_]
#         return Response(serialize_sqlalchemy_obj(vehicles_), status=status.HTTP_200_OK)


class VehicleDetailViewSet(viewsets.ModelViewSet):
    queryset = VehicleDetail.objects.all()
    serializer_class = VehicleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
