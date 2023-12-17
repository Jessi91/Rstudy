from django import forms
from .models import *

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

class ParticipationForumForm(forms.ModelForm):
    class Meta:
        model = ParticipationForum
        fields = ['titre_msg', 'contenu']
        widgets = {
            'titre_msg': forms.TextInput(attrs={'placeholder': 'Titre du message'}),
            'contenu': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Contenu du message'}),
        }
        labels = {
            'titre_msg': 'Titre',
            'contenu': 'Message',
        }