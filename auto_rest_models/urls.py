from django.urls import path, include
from rest_framework.routers import DefaultRouter

from auto_rest_models.views import GenericModelViewSet

router = DefaultRouter()
router.register(
    r'(?P<app_name>\w+)/(?P<model_name>[a-z]+)',
    GenericModelViewSet,
    'models',
)

urlpatterns = [
    path('', include(router.urls)),
]
