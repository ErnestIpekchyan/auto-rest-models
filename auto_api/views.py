from django.apps import apps
from rest_framework import viewsets

from auto_api.serializers import get_generic_serializer


class GenericModelViewSet(viewsets.ModelViewSet):

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        app_name = self.kwargs['app_name']
        model_name = self.kwargs['model_name']
        self.model_class = apps.get_model(app_name, model_name)

    def get_queryset(self):
        return self.model_class.objects.all()

    def get_serializer_class(self):
        return get_generic_serializer(self.model_class)
