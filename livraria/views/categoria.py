from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["descrição"]
    search_fields = ["descrição"]
    ordering_fields = ["descrição"]
    ordering = ["descrição"]