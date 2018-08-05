from django.forms import ModelForm
from . import models


class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'