from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    tamanho = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produtos"
