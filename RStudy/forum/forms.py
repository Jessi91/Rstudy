from django import forms
from .models import Forum, ParticipationForum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['nom', 'description', 'ouvert']
        labels = {
            'nom': 'Nom du forum',
            'description': 'Description du forum',
            'ouvert': 'Ouvert'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # Augmenter les dimensions ici
        }

class ParticipationForumForm(forms.ModelForm):
    class Meta:
        model = ParticipationForum
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Contenu du message'}),
        }
        labels = {
            'contenu': 'Message',
        }
