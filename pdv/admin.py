from django.contrib import admin
from .models import Caixa


@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = ("id", "operador", "aberto", "valor_inicial", "abertura_em", "fechamento_em")
    list_filter = ("aberto", "abertura_em")
    search_fields = ("id", "operador__username")