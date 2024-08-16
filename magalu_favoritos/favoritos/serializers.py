from rest_framework import serializers
from .models import Cliente, Produto, Favorito

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'titulo', 'image_url', 'preco', 'review']

class FavoritoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = Favorito
        fields = ['produto']