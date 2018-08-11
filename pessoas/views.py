from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from . import forms

# Create your views here.

def home(request):
    return render(request, 'index.html')


@login_required
def person_list(request):
    persons = models.Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})


@login_required
def person_new(request):
    form = forms.PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_new.html', {'form': form})


@login_required
def person_edit(request, id):
    person = get_object_or_404(models.Person, pk=id)
    form = forms.PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_new.html', {'form': form})


@login_required
def person_delete(request, id):
    person = get_object_or_404(models.Person, pk=id)
    
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete.html', {'person':person})