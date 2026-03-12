from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto


class MovimentacaoEstoque(models.Model):

    TIPO_MOVIMENTO = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
        ('A', 'Ajuste'),
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_MOVIMENTO)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    data = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.get_tipo_display()} - {self.quantidade}"
