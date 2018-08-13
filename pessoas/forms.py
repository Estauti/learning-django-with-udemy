from django.forms import ModelForm
from . import models


class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'

class DocumentForm(ModelForm):
    class Meta:
        model = models.Document
        fields = '__all__'

class HouseForm(ModelForm):
    class Meta:
        model = models.House
        fields = '__all__'