from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    imagem_url = models.URLField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Favorito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='favoritos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cliente', 'produto')

    def __str__(self):
        return f"{self.cliente.nome} - {self.produto.titulo}"