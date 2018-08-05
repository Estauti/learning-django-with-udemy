from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms

# Create your views here.

def home(request):
    return render(request, 'pessoas/index.html')

def person_list(request):
    persons = models.Person.objects.all()
    return render(request, 'pessoas/person_list.html', {'persons': persons})

def person_new(request):
    form = forms.PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'pessoas/person_new.html', {'form': form})

def person_edit(request, id):
    person = get_object_or_404(models.Person, pk=id)
    form = forms.PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'pessoas/person_new.html', {'form': form})

def person_delete(request, id):
    person = get_object_or_404(models.Person, pk=id)
    
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'pessoas/person_delete.html', {'person':person})