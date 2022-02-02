from django.shortcuts import render, redirect
from .forms import DecadeForm, FadForm
from .models import Decade, Fad 
# Create your views here.


def decade_get(request):
    decade = Decade.objects.all()
    return render(request, 'nostal/decade_get.html', {'decade': decade})

def fad_get(request):
    fad = Fad.objects.all()
    return render(request, 'nostal/fad_get.html', {'fad': fad})

def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostal/decade_detail.html', {'decade': decade})

def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostal/fad_detail.html', {'fad': fad})

def decade_create(request):
    form = DecadeForm()
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form: DecadeForm()
    return render(request, 'nostal/decade_form.html', {'form': form})

def fad_create(request):
    form = FadForm()
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form: FadForm()
    return render(request, 'nostal/fad_form.html', {'form': form})

def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == 'POST':
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostal/decade_form.html', {'form': form})

def fad_edit(request, pk):
    fad = Fad.objects.get(pk=pk)
    if request.method == 'POST':
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostal/fad_form.html', {'form': form})

def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_get')

def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('decade_get')