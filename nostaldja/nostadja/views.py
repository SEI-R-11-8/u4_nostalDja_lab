from django.shortcuts import render, redirect
from .forms import FadsForm, DecadeForm
from .models import Decade, Fads

# Create your views here.


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostadja/decade_list.html', {'decades': decades})


def fads_list(request):
    fads = Fads.objects.all()
    return render(request, 'nostadja/fads_list.html', {'fads': fads})


def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostadja/decade_detail.html', {'decade': decade})


def fads_detail(request, pk):
    fads = Fads.objects.get(id=pk)
    return render(request, 'nostadja/fads_detail.html', {'fads': fads})


def fads_edit(request, pk):
    fads = Fads.objects.get(pk=pk)
    if request.method == "POST":
        form = FadsForm(request.POST, instance=fads)
        if form.is_valid():
            fads = form.save()
            return redirect('fads_detail', pk=fads.pk)
    else:
        form = FadsForm(instance=fads)
    return render(request, 'nostadja/fads_form.html', {'form': form})


def decade_edit(request, pk):
    decade = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostadja/decade_form.html', {'form': form})


def fads_create(request):
    if request.method == 'POST':
        form = FadsForm(request.POST)
        if form.is_valid():
            fads = form.save()
            return redirect('fads_detail', pk=fads.pk)
    else:
        form = FadsForm()
    return render(request, 'nostadja/fads_form.html', {'form': form})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostadja/decade_form.html', {'form': form})


def fads_delete(request, pk):
    Fads.objects.get(id=pk).delete()
    return redirect('fads_list')


def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')
