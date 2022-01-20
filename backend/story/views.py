# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from article.serializers import ArticleDetailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from story.models import Slides, Vehicles, VehicleDetail
# from rest_framework.permissions import IsAdminUser
from story.permissions import IsAdminUserOrReadOnly
from story.serializers import SlidesSerializer, VehiclesSerializer, VehicleDetailSerializer


# from article.serializers import ArticleListSerializer


class StroyViewSet(viewsets.ModelViewSet):
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


class VehicleDetailViewSet(viewsets.ModelViewSet):
    queryset = VehicleDetail.objects.all()
    serializer_class = VehicleDetailSerializer
