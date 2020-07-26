from django.apps import apps
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from auto_api.serializers import get_generic_serializer


class GenericModelViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.model_class = self.get_model_class()

    def get_model_class(self):
        app_name = self.kwargs['app_name']
        model_name = self.kwargs['model_name']
        return apps.get_model(app_name, model_name)

    def get_queryset(self):
        return self.model_class.objects.all()

    def get_serializer_class(self):
        return get_generic_serializer(self.model_class)
