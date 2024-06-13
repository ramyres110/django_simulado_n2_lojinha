from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    preco = models.FloatField()
    informacoes = models.TextField()
    ativo = models.BooleanField()
    quantidade = models.IntegerField()
    img_url_principal = models.TextField(default="")
    img_url_secundaria = models.TextField(default="")
    img_url_lateral = models.TextField(default="")
    img_url_superior = models.TextField(default="")
    link_compra = models.URLField(null=True)

    def __str__(self) -> str:
        return f"{self.id} | {self.descricao}"


class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} | {self.nome} | {self.email}"


class Promocao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    novo_preco = models.FloatField(null=True)

    def __str__(self) -> str:
        return f"{self.produto} | {self.novo_preco}"