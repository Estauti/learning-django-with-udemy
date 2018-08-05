from django.db import models
from django.conf import settings

# Create your models here.

class Person(models.Model):
    nome_completo = models.CharField(max_length=80)
    idade = models.PositiveIntegerField()
    data_de_nascimento = models.DateField()
    foto = models.ImageField(upload_to='fotos_pessoas')

    def __str__(self):
        return self.nome_completo