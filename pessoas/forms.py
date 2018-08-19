from django.forms import ModelForm
from . import models

class DocumentForm(ModelForm):
    class Meta:
        model = models.Document
        fields = '__all__'

class HouseForm(ModelForm):
    class Meta:
        model = models.House
        fields = '__all__'

class PersonForm(ModelForm):    
    def __init__(self, unused_documents, *args, **kwargs):
        super (PersonForm, self).__init__(*args, **kwargs)
        if unused_documents:
            self.fields['document'].queryset = models.Document.objects.filter(person__isnull=True)
    
    class Meta:
        model = models.Person
        fields = '__all__'