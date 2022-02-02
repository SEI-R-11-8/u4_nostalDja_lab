import imp
from django.shortcuts import render, redirect
from .models import Decade, Fad
from .form import DecadeForm, FadForm


# Create your views here.
def decade_render (request):
    decade = Decade.objects.all()
    return render(request, 'decade_render.html', {'decade': decade})

def fad_render (request):
    fad = Fad.objects.all()
    return render(request, 'fad_render.html', {'fad': fad})

def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'decade_detail.html', {'decade': decade})

def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'fad_detail.html', {'fad': fad})

def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'decade_form.html', {'form': form})

def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'Fad_form.html', {'form': form})

def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'decade_form.html', {'form': form})

def fad_edit(request, pk):
    fad = Fad.objects.get(pk=pk)
    if request.method == "POST":
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'fad_form.html', {'form': form})

def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_render')

def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_render')