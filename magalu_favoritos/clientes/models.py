from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
class ProdutoFavorito(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='favoritos', on_delete=models.CASCADE)
    produto_id = models.CharField(max_length=255)
    produto_nome = models.CharField(max_length=255)
    produto_imagem = models.URLField()
    produto_preco = models.DecimalField(max_digits=10, decimal_places=2)
    produto_review = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.produto_nome} - {self.cliente.nome}'