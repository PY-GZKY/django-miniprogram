from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user_info.views import UserViewSet


router = DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^', include('comment.urls'),name="comment"),
    url(r'^', include('scenic.urls'),name="scenic"),
    url(r'^', include('user_info.urls'),name="user_info"),

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
