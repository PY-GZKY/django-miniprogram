from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from story import views

router = DefaultRouter()
router.register(r'slides', views.SlidesViewSet)
router.register(r'vehicles', views.VehiclesViewSet)
router.register(r'vehicles_detail', views.VehicleDetailViewSet)
router.register(r'stories', views.StoriesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
