from django.shortcuts import render,redirect
from .forms import decadeForm,FadForm


# Create your views here.
# tunr/views.py

from .models import decade,Fad

def decade_list(request):
    decades = decade.objects.all()
    return render(request, 'nostalDja/decade_list.html', {'decades': decades})


def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostalDja/fad_list.html', {'fads': fads})


def decade_detail(request, pk):
    decades = decade.objects.get(id=pk)
    return render(request, 'nostalDja/decade_detail.html', {'decades': decades})

def fad_detail(request, pk):
    fads = Fad.objects.get(id=pk)
    return render(request, 'nostalDja/fad_detail.html', {'fads': fads})


def decade_create(request):
    if request.method == 'POST':
        form = decadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = decadeForm()
    return render(request, 'nostalDja/decade_form.html', {'form': form})

def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostalDja/fad_form.html', {'form': form})

def decade_delete(request, pk):
    decade.objects.get(id=pk).delete()
    return redirect('decade_list')


def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
    