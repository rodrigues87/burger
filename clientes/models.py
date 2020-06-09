from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    field_name = models.EmailField(max_length=254)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Clientes"
