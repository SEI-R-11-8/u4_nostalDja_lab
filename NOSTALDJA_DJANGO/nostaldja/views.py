from django.shortcuts import render
from .models import Decade, Fad

# Create your views here.

def decade_list(req):
  decades = Decade.objects.all()
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