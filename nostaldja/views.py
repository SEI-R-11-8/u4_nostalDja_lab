from django.shortcuts import render, redirect

# Create your views here.
from .models import Decades, Fads
from .forms import DecadeForm, FadForm

def decade_list(request):
    decades = Decades.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})

def decade_detail(request, pk):
    decades = Decades.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decades': decades})

def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decades = form.save()
            return redirect('decade_detail, pk=decade.pk')
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})

def decade_edit(request, pk):
    decade = Decades.objects.get(pk=pk)
    if request.method == 'POST':
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail, pk=decade.pk')
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_form.html', {'form': form})


def decade_delete(request, pk):
    Decades.objects.get(id=pk).delete()
    return redirect('decade_list')

def fad_list(request):
    fads = Fads.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})

def fad_detail(request):
    fads = Fads.objects.all()
    return render(request, 'nostaldja/fad_detail.html', {'fads': fads})

def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail, pk=fad.pk')
    else:
        form = FadForm()
    return render(request, 'nostaldja/fad_form.html', {'form': form})

def fad_edit(request, pk):
    fad = Fads.objects.get(pk=pk)
    if request.method == 'POST':
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail, pk=fad.pk')
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja/fad_form.html', {'form': form})

def fad_delete(request, pk):
    Fads.objects.get(id=pk).delete()
    return redirect('fad_list')