from django.apps import apps
from rest_framework import viewsets


class GenericModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        app_name = self.kwargs['app_name']
        model_name = self.kwargs['model_name']
        model_class = apps.get_model(app_name, model_name)
        return model_class.objects.all()

    def get_serializer_class(self):
        pass
