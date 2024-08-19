from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cliente, ProdutoFavorito
from .serializers import ClienteSerializer, ProdutoFavoritoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutoFavoritoViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFavorito.objects.all()
    serializer_class = ProdutoFavoritoSerializer
    def get_queryset(self):
        cliente_id = self.request.query_params.get('cliente_id')
        if cliente_id:
            return ProdutoFavorito.objects.filter(cliente_id=cliente_id)
        else:
            return ProdutoFavorito.objects.none()


class RemoverProdutoFavorito(APIView):
    def delete(self, request, cliente_id, produto_id):
        try:
            # Tenta encontrar o produto favorito para o cliente específico
            produto_favorito = ProdutoFavorito.objects.get(cliente_id=cliente_id, produto_id=produto_id)
            produto_favorito.delete()  # Remove o produto favorito da lista
            return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna sucesso com conteúdo vazio
        except ProdutoFavorito.DoesNotExist:
            return Response({"error": "Produto não encontrado na lista de favoritos"}, status=status.HTTP_404_NOT_FOUND)
