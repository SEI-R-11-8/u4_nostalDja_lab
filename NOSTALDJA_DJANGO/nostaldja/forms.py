from django import forms
from .models import Decade, Fad

class DecadeForm(forms.ModelForm):

  class Meta:
    model = Decade
    fields = ('start_year',)

class FadForm(forms.ModelForm):
  decade = forms.ModelChoiceField(queryset=Decade.objects.order_by('start_year'))

  class Meta:
    model = Fad
    fields = ('name', 'image_url', 'description', 'decade')