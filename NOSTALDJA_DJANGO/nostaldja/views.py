from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm

# Create your views here.

def decade_list(req):
  decades = Decade.objects.all().order_by('start_year')
  return render(req, 'nostaldja/decade_list.html', {'decades': decades})

def fad_list(req):
  fads = Fad.objects.all().order_by('name')
  return render(req, 'nostaldja/fad_list.html', {'fads': fads})

def decade_details(req, pk):
  decade = Decade.objects.get(id=pk)
  return render(req, 'nostaldja/decade_details.html', {'decade': decade})

def fad_details(req, pk):
  fad = Fad.objects.get(id=pk)
  return render(req, 'nostaldja/fad_details.html', {'fad': fad})

def decade_create(req):
  if req.method == 'POST':
    form = DecadeForm(req.POST)
    if form.is_valid():
      decade = form.save()
      return redirect('decade_details', pk=decade.pk)
  else:
    form = DecadeForm()
  return render(req, 'nostaldja/decade_form.html', {'form': form})

def fad_create(req):
  if req.method == 'POST':
    form = FadForm(req.POST)
    if form.is_valid():
      fad = form.save()
      return redirect('fad_details', pk=fad.pk)
  else:
    form = FadForm()
  return render(req, 'nostaldja/fad_form.html', {'form': form})

def decade_edit(req, pk):
  decade = Decade.objects.get(pk=pk)
  if req.method == "POST":
    form = DecadeForm(req.POST, instance=decade)
    if form.is_valid():
      decade = form.save()
      return redirect('decade_details', pk=decade.pk)
  else:
    form = DecadeForm(instance=decade)
  return render(req, 'nostaldja/decade_form.html', {'form': form})

def fad_edit(req, pk):
  fad = Fad.objects.get(pk=pk)
  if req.method == "POST":
    form = FadForm(req.POST, instance=fad)
    if form.is_valid():
      fad = form.save()
      return redirect('fad_details', pk=fad.pk)
  else:
    form = FadForm(instance=fad)
  return render(req, 'nostaldja/fad_form.html', {'form': form})

def decade_delete(req, pk):
  Decade.objects.get(id=pk).delete()
  return redirect('decade_list')

def fad_delete(req, pk):
  Fad.objects.get(id=pk).delete()
  return redirect('fad_list')
