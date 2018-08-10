from django.db import models
from django.conf import settings

# Create your models here.

class Document(models.Model):
    identification = models.CharField(max_length=30)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identification

class Person(models.Model):
    name = models.CharField(max_length=80)
    height = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='fotos_pessoas')
    document = models.OneToOneField(Document, on_delete=models.CASCADE)

    def __str__(self):
        return self.name