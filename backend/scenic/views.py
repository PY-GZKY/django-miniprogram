# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from article.serializers import ArticleDetailSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
# from article.serializers import ArticleListSerializer
from rest_framework.views import APIView

from django_mini import settings
from scenic.models import Article
from scenic.models import Avatar
from scenic.models import Category
from scenic.models import Tag
# from rest_framework.permissions import IsAdminUser
from scenic.permissions import IsAdminUserOrReadOnly
from scenic.serializers import ArticleDetailSerializer
from scenic.serializers import ArticleSerializer
from scenic.serializers import AvatarSerializer
from scenic.serializers import CategorySerializer, CategoryDetailSerializer
from scenic.serializers import TagSerializer
from snippets.utils import serialize_sqlalchemy_obj


class ScenicListAPIView(APIView):
    """
    ScenicListAPIView
    """
    def get(self, request, format=None):
        scenic_list = settings.mongo_client.chao.museum_scenic.find({"data_source":"携程"}).limit(8)
        items = [item for item in scenic_list]
        items = {"items": serialize_sqlalchemy_obj(items)}
        # print(items)
        return Response(items, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer = BookInfoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BannerInfoView(APIView):
    """
    BannerInfoView
    """

    def get(self, request, format=None):
        items = {"banners": [
            "http://img4.youxiake.com/ps/2021/11/one/20eb546d5b21e3486b898feac1ee2b1a.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/e4427d9289e73f99acd2b4e4972c6d94.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/6f300ae31999c9034ae1d70ea81da442.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/1cb5974d4f3d216c810122097ef6b804.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/20eb546d5b21e3486b898feac1ee2b1a.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/e4427d9289e73f99acd2b4e4972c6d94.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/6f300ae31999c9034ae1d70ea81da442.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/1cb5974d4f3d216c810122097ef6b804.jpg"
        ]}
        return Response(items, status=status.HTTP_200_OK)

class HotInfoView(APIView):
    """
    HotInfoView
    """

    def get(self, request, format=None):
        items = {"hot": [
            "http://img4.youxiake.com/ps/2021/11/one/20eb546d5b21e3486b898feac1ee2b1a.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/e4427d9289e73f99acd2b4e4972c6d94.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/6f300ae31999c9034ae1d70ea81da442.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/1cb5974d4f3d216c810122097ef6b804.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/20eb546d5b21e3486b898feac1ee2b1a.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/e4427d9289e73f99acd2b4e4972c6d94.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/6f300ae31999c9034ae1d70ea81da442.jpg",
            "http://img4.youxiake.com/ps/2021/11/one/1cb5974d4f3d216c810122097ef6b804.jpg"
        ]}
        return Response(items, status=status.HTTP_200_OK)



class AvatarViewSet(viewsets.ModelViewSet):
    """
    上传封面视图
    """
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    """
    标签
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """博文视图集"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

    # filterset_fields = ['author__username', 'title']

    # def get_queryset(self):
    #     queryset = self.queryset
    #     username = self.request.query_params.get('username', None)
    #
    #     if username is not None:
    #         queryset = queryset.filter(author__username=username)
    #
    #     return queryset

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ArticleListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetail(APIView):
#     """文章详情视图"""
#
#     def get_object(self, pk):
#         """获取单个文章对象"""
#         try:
#             return Article.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """文章详情视图"""
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
