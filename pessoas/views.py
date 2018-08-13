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

@login_required
def document_list(request):
    docs = models.Document.objects.all()
    return render(request, 'document_list.html', {'docs':docs})

@login_required
def document_new(request):
    form = forms.DocumentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('document_list')
    return render(request, 'document_new.html', {'form':form})

@login_required
def document_edit(request, id):
    doc = get_object_or_404(models.Document, pk=id)
    form = forms.DocumentForm(request.POST or None, instance=doc)

    if form.is_valid():
        form.save()
        return redirect('document_list')
    return render(request, 'document_new.html', {'form': form})

@login_required
def document_delete(request, id):
    doc = get_object_or_404(models.Document, pk=id)

    if request.method == 'POST':
        doc.delete()
        return redirect('document_list')
    return render(request, 'document_delete.html', {'doc':doc})

@login_required
def house_list(request):
    houses = models.House.objects.all()
    return render(request, 'house_list.html', {'houses':houses})

@login_required
def house_new(request):
    form = forms.HouseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('house_list')
    return render(request, 'house_new.html', {'form':form})

@login_required
def house_edit(request, id):
    house = get_object_or_404(models.House, pk=id)
    form = forms.HouseForm(request.POST or None, request.FILES or None, instance=house)

    if form.is_valid():
        form.save()
        return redirect('house_list')
    return render(request, 'house_new.html', {'form':form})

@login_required
def house_delete(request, id):
    house = get_object_or_404(models.House, pk=id)

    if request.method == 'POST':
        house.delete()
        return redirect('house_list')
    return render(request, 'house_delete.html', {'house':house})