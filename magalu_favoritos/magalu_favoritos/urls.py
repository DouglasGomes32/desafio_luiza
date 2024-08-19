from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import (
    ClienteViewSet,
    ProdutoFavoritoViewSet,
    RemoverProdutoFavorito
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos_favoritos', ProdutoFavoritoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(router.urls)), 
    path('produtos_favoritos/<int:cliente_id>/<int:produto_id>/', RemoverProdutoFavorito.as_view(), name='remover_produto_favorito'),
]