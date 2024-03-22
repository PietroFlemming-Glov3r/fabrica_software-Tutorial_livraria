from rest_framework.serializers import ModelSerializer, CharField

from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        usuario = CharField(source="usuario.email", read_only=True)
        fields = "__all__"