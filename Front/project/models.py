from django.db import models

class Estoque(models.Model):
    localizacao = models.CharField(max_length=100)  # Localização do estoque
    setor = models.CharField(max_length=50)  # Setor do estoque

    def __str__(self):
        return f"{self.localizacao} - {self.setor}"

class Produto(models.Model):
    nome = models.CharField(max_length=100)  # Nome do produto
    descricao = models.TextField(blank=True, null=True)  # Descrição do produto (opcional)
    quantidade_estoque = models.IntegerField()  # Quantidade em estoque
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço unitário (campo monetário)
    data_adicao = models.DateTimeField(auto_now_add=True)  # Data de adição (gerada automaticamente)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name="produtos")  # Relacionamento com Estoque

    def __str__(self):
        return self.nome