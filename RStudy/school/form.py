# forms.py
from django import forms
from .models import EspacePersonnel

class EspacePersonnelForm(forms.ModelForm):
    class Meta:
        model = EspacePersonnel
        fields = ['dashboard', 'calendrier', 'notes']
