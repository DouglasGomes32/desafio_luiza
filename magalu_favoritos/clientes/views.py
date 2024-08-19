from rest_framework import viewsets # type: ignore
from .models import Cliente, ProdutoFavorito
from .serializers import ClienteSerializer, ProdutoFavoritoSerializer # type: ignore


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoFavoritoViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFavorito.objects.all()
    serializer_class = ProdutoFavoritoSerializer