from django.db import models
from django.conf import settings

# Create your models here.

class Document(models.Model):
    identification = models.CharField(max_length=30)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identification

class School(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=80)
    height = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='fotos_pessoas')
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    schools = models.ManyToManyField(School, blank=True)

    def __str__(self):
        return self.name

class House(models.Model):
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    photo = models.ImageField(upload_to='fotos_casas')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description