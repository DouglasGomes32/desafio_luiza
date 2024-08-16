from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cliente, Produto, Favorito
from .serializers import ClienteSerializer, ProdutoSerializer, FavoritoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

class FavoritoViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, cliente_id=None):
        favoritos = Favorito.objects.filter(cliente_id=cliente_id)
        serializer = FavoritoSerializer(favoritos, many=True)
        return Response(serializer.data)
    
    def create(self, request, client_id=None):
        cliente = Cliente.objects.get(pk=client_id)
        produto_id = request.data.get('produto_id')
        produto = Produto.objects.get(pk=produto_id)
        favorito, created = Favorito.objects.get_or_create(cliente=cliente, produto=produto)
        if not created:
            return Response({'message': "Produto já esta nos favoritos"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(FavoritoSerializer(favorito).data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, cliente_id=None, produto_id=None):
        favorito = Favorito.objects.filter(cliente_id=cliente_id, produto_id=produto_id)
        if favorito.exists():
            favorito.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Produto não encontrado na lista de favoritos"}, status=status.HTTP_404_NOT_FOUND)