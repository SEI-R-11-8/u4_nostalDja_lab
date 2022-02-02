from django import forms
from .models import Fad

class FadForm(forms.ModelForm):
    class Meta:
        model = Fad
        fields = ('decade', 'name', 'image_url', 'description')