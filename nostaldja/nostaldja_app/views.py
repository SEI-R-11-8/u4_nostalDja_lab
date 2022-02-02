from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import FadForm

# Create your views here.
def decade_get_all(req):
    decades = Decade.objects.all()
    return render(req, 'decade/decade_get_all.html', {'decades': decades})

def fads_by_decade(req, fk):
    fads = Fad.objects.filter(decade_id=fk)
    decade = Decade.objects.get(id=fk)
    return render(req, 'fad/fads_by_decade.html', {'fads':fads, 'decade':decade})
def fad_create(req):
    if req.method == 'POST':
        form = FadForm(req.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fads_by_decade', fk=fad.decade_id)
    else:
        form = FadForm()
    return render(req, 'fad/fad_form.html', {'form':form})
def fad_edit(req, id):
    fad = Fad.objects.get(id=id)
    if req.method == 'POST':
        form = FadForm(req.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fads_by_decade', fk=fad.decade_id)
    else:
        form = FadForm(instance=fad)
    return render(req, 'fad/fad_form.html', {'form':form})
def fad_delete(req, id):
    fad = Fad.objects.get(id=id)
    Fad.objects.get(id=id).delete()
    return redirect('fads_by_decade', fk=fad.decade_id)