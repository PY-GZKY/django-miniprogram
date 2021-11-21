from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, generics, mixins
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from django_mini import settings
from snippets.models import Snippet, Entitie
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer, EntitieSerializer
from .models import BookInfo
from .serializers import BookInfoSerializer


def global_setting(request):
    """
    将settings里面的变量 注册为全局变量
    """
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_YEAR': settings.SITE_YEAR,
        'SITE_META_DESCRIPTION': settings.SITE_META_DESCRIPTION,
        'SITE_META_KEYWORDS': settings.SITE_META_KEYWORDS,
        'SITE_HOME_TITLE': settings.SITE_HOME_TITLE,
        'SITE_MAIL': settings.SITE_MAIL,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_TYPE_CHINESE': settings.SITE_TYPE_CHINESE,
        'SITE_TYPE_ENGLISH': settings.SITE_TYPE_ENGLISH,
        'SITE_DOMAIN_URL': settings.SITE_DOMAIN_URL,
        'SITE_AVATAR': settings.SITE_AVATAR,
        'ABOUT_NAME': settings.ABOUT_NAME,
        'ABOUT_DESC': settings.ABOUT_DESC
    }


# class BookListAPIView(generics.ListCreateAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


class BookListAPIView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class BookListAPIView(APIView):
#     def get(self, request, format=None):
#         snippets = BookInfo.objects.all()
#         serializer = BookInfoSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BookInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntitieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Entitie.objects.all()
    serializer_class = EntitieSerializer
