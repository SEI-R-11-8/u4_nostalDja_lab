from django.shortcuts import render, redirect

# Create your views here.
from .forms import DecadeForm, FadForm
from .models import Decade, Fad


def decade_list(req):
    decades = Decade.objects.all()
    return render(req, 'nostaldja/decade_list.html', {'decades': decades})


def decade_detail(req, pk):
    decade = Decade.objects.get(id=pk)
    return render(req, 'nostaldja/decade_detail.html', {'decade': decade})


def decade_create(req):
    if req.method == 'POST':
        form = DecadeForm(req.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(req, 'nostaldja/decade_form.html', {'form': form})


def decade_edit(req, pk):
    decade = Decade.objects.get(pk=pk)
    if req.method == 'POST':
        form = DecadeForm(req.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(req, 'nostaldja/decade_form.html', {'form': form})


def decade_delete(req, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')


def fad_list(req):
    fads = Fad.objects.all()
    return render(req, 'nostaldja/fad_list.html', {'fads': fads})


def fad_detail(req, pk):
    fad = Fad.objects.get(id=pk)
    return render(req, 'nostaldja/fad_detail.html', {'fad': fad})


def fad_create(req):
    if req.method == 'POST':
        form = FadForm(req.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = DecadeForm()
    return render(req, 'nostaldja/fad_form.html', {'form': form})


def fad_edit(req, pk):
    fad = Fad.objects.get(pk=pk)
    if req.method == 'POST':
        form = FadForm(req.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(req, 'nostaldja/fad_form.html', {'form': form})


def fad_delete(req, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
