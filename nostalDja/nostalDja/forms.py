# tunr/forms.py
from django import forms
from .models import decade,Fad

class decadeForm(forms.ModelForm):

    class Meta:
        model = decade
        fields = ('name',)

class FadForm(forms.ModelForm):

    class Meta:
        model = Fad
        fields = ('name', 'description', 'image_url', 'decade')