from django.shortcuts import render
from .models import Decade, Fad

# Create your views here.
def decade_get_all(req):
    decades = Decade.objects.all()
    return render(req, 'decade/decade_get_all.html', {'decades': decades})

def fad_by_decade(req, fk):
    fads = Fad.objects.filter(decade_id=fk)
    decade = Decade.objects.get(id=fk)
    return render(req, 'fad/fads_by_decade.html', {'fads':fads, 'decade':decade})