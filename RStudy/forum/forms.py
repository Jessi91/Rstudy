from django import forms
from .models import Forum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['nom', 'description', 'ouvert', 'participants']
        labels = {
            'nom': 'Nom du forum',
            'description': 'Description du forum',
            'ouvert': 'Ouvert',
            'participants': 'Participants',
        }
