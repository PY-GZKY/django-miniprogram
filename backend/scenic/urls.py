from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from scenic import views

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'avatar', views.AvatarViewSet)

urlpatterns = [
    url(r'^scenic/', include(router.urls)),
    url(r'^scenic_list/$', views.ScenicListAPIView.as_view()),
    url(r'^banner_info/$', views.BannerInfoView.as_view()),
    url(r'^hot_info/$', views.HotInfoView.as_view()),
]
