from django.contrib import admin
from .models import MovimentacaoEstoque


@admin.register(MovimentacaoEstoque)
class MovimentacaoAdmin(admin.ModelAdmin):

    list_display = ('produto', 'tipo', 'quantidade', 'data')
    list_filter = ('tipo', 'data')
