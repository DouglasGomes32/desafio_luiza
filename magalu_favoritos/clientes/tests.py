from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Cliente, ProdutoFavorito

class ClienteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cliente_data = {'nome': 'João Silva', 'email': 'joao@example.com'}
        self.cliente = Cliente.objects.create(**self.cliente_data)

    def test_criar_cliente(self):
        response = self.client.post(reverse('clientes-list'), {'nome': 'Maria Oliveira', 'email': 'maria@example.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)

    def test_atualizar_cliente(self):
        updated_data = {'nome': 'João da Silva', 'email': 'joao@example.com'}
        response = self.client.put(reverse('clientes-detail', kwargs={'pk': self.cliente.pk}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, 'João da Silva')

class ProdutoFavoritoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cliente = Cliente.objects.create(nome='João Silva', email='joao@example.com')
        self.produto_data = {'cliente': self.cliente, 'produto_id': 1}
        self.produto_favorito = ProdutoFavorito.objects.create(**self.produto_data)

    def test_adicionar_produto_favorito(self):
        novo_produto_data = {'cliente': self.cliente.pk, 'produto_id': 2}
        response = self.client.post(reverse('produtos_favoritos-list'), novo_produto_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProdutoFavorito.objects.count(), 2)

    def test_listar_produtos_favoritos(self):
        response = self.client.get(reverse('produtos_favoritos-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Apenas 1 produto favorito está presente

    def test_remover_produto_favorito(self):
        response = self.client.delete(reverse('remover_produto_favorito', kwargs={'cliente_id': self.cliente.pk, 'produto_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ProdutoFavorito.objects.count(), 0 )