from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from scenic import views

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'avatar', views.AvatarViewSet)


urlpatterns = [
    url(r'^scenic/', include(router.urls))
]
