from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from comment import views
router = DefaultRouter()
router.register(r'comment', views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]