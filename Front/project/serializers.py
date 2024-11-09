from rest_framework import serializers
from .models import Produto, Estoque

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    # Para exibir os detalhes do estoque ao invés do ID
    estoque = EstoqueSerializer(read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'
