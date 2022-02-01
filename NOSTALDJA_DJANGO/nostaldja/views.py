from django.shortcuts import render
from .models import Decade, Fad

# Create your views here.

def decade_list(req):
  decades = Decade.objects.all()
  return render(req, 'nostaldja/decade_list.html', {'decades': decades})

def fad_list(req):
  fads = Fad.objects.all()
  return render(req, 'nostaldja/fad_list.html', {'fads': fads})