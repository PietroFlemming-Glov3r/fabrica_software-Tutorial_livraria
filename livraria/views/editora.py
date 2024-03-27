from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Editora
from livraria.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["nome", "site"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "site"]
    ordering = ["nome"]
