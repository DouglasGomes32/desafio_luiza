from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ProductViewSet, FavoritoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'produtos', ProductViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
    path('clientes/<int:cliente_id>/favoritos/', FavoritoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('clientes/<int:cliente_id>/favorotos/<int:produto_id>/', FavoritoViewSet.as_view({'delete': 'destroy'})),
]