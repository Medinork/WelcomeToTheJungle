from django.contrib import admin
from .models import Produto, Estoque

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_estoque', 'preco', 'data_adicao', 'estoque')
    search_fields = ('nome', 'descricao')
    list_filter = ('data_adicao', 'estoque')
    date_hierarchy = 'data_adicao'

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'setor')
    search_fields = ('localizacao', 'setor')
