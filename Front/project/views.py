from rest_framework import viewsets
from .models import Produto, Estoque
from .serializers import ProdutoSerializer, EstoqueSerializer



class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
