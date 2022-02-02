from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm
# Create your views here.


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})


def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form, 'submit_button_text': 'Create'})


def decade_edit(request, pk):
    decade = Decade.objects.get(id=pk)
    if request.method == 'POST':
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_form.html', {'form': form, 'submit_button_text': 'Save'})


def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})


def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})


def fad_create(request, pk):
    decade = Decade.objects.get(id=pk)

    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = FadForm({'decade': decade})
    return render(request, 'nostaldja/fad_form.html', {'form': form})


def fad_edit(request, pk):
    fad = Fad.objects.get(id=pk)

    if request.method == 'POST':
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja/fad_form.html', {'form': form})
