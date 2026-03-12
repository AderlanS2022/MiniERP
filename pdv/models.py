from django.db import models
from django.conf import settings


class Caixa(models.Model):
    operador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="caixas")
    aberto = models.BooleanField(default=True)

    abertura_em = models.DateTimeField(auto_now_add=True)
    fechamento_em = models.DateTimeField(null=True, blank=True)

    valor_inicial = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        status = "ABERTO" if self.aberto else "FECHADO"
        return f"Caixa #{self.id} - {status}"