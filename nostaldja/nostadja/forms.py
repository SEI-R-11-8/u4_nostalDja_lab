from django import forms
from .models import Decade, Fads


class DecadeForm(forms.ModelForm):

    class Meta:
        model = Decade
        fields = ('start_year',)


class FadsForm(forms.ModelForm):

    class Meta:
        model = Fads
        fields = ('name', 'image_url', 'description', 'decade',)
