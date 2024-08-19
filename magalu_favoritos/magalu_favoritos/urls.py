from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from clientes.views import ClienteViewSet, ProdutoFavoritoViewSet
from django.urls import path
from magalu_favoritos.views import ( # type: ignore
    ClienteListCreateView,
    ClienteRetrieveUpdateDeleteView,
    ProdutoFavoritoListCreateView,
    RemoverProdutoFavorito
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos_favoritos', ProdutoFavoritoViewSet)

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='clientes'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDeleteView.as_view(), name='cliente-detail'),
    path('produtos_favoritos/', ProdutoFavoritoListCreateView.as_view(), name='produtos_favoritos'),
    path('produtos_favoritos/<int:cliente_id>/<int:produto_id>/', RemoverProdutoFavorito.as_view(), name='remover_produto_favorito'),
]