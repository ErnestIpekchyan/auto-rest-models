from rest_framework import viewsets


class GenericModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        pass

    def get_serializer_class(self):
        pass
