from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_swagger_view(title='Snippets API')

urlpatterns = [
    re_path('^$', schema_view),
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
