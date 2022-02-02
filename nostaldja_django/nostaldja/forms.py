from django import forms
from .models import Fad

class FadForm(forms.ModelForm):

    class Meta:
        model = Fad
        fields = ('name', 'description', 'image_url','decade')