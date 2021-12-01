from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from user_info import views
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]