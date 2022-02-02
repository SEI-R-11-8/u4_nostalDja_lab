from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm

# Create your views here.

def decade_list(req):
  decades = Decade.objects.all().order_by('start_year')
  return render(req, 'nostaldja/decade_list.html', {'decades': decades})

def fad_list(req):
  fads = Fad.objects.all()
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
      return redirect('decade_detail', pk=decade.pk)
  else:
    form = DecadeForm()
  return render(req, 'nostaldja/decade_form.html', {'form': form})