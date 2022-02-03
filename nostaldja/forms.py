# tunr/forms.py
from django import forms
from .models import Decades, Fads

class DecadeForm(forms.DecadeForm):

    class Meta:
        model = Decades
        fields = ('start_year',)

class FadForm(forms.FadForm):

    class Meta:
        model = Fads
        fields = ('name', 'image_url', 'description', 'decade')