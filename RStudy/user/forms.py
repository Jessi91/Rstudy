# authentication/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

LABELS = {
            'email': 'Adresse Email',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe',
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            '_sexe_f': 'Sexe',
            '_date_naissance': 'Date de Naissance',
            '_adresse': 'Adresse',
            '_num_tel': 'Numéro de Téléphone',
        }

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', '_sexe_f', '_date_naissance', '_adresse', '_num_tel')
        # Pour que la datte de naissance soit comprise entre 1900 et 2100
        _date_naissance = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
        LABELS

class ReadUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', '_sexe_f', '_date_naissance', '_adresse', '_num_tel')
        LABELS
        



