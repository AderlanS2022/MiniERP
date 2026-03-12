from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):

    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, blank=True, null=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    estoque = models.IntegerField(default=0)

    imagem = models.ImageField(
        upload_to='produtos/',
        blank=True,
        null=True
    )

    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
