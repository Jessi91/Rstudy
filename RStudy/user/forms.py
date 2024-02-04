# authentication/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from home.models import EnregistrementFormation


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'sexe_f', 'date_naissance', 'adresse', 'num_tel')


class LoginForm(forms.Form):
    email = forms.CharField(max_length=63, widget=forms.EmailInput, label='Email')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class ReadUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'sexe_f', 'date_naissance', 'adresse', 'num_tel')


class EnregistrementFormationForm(forms.ModelForm):
    class Meta:
        model = EnregistrementFormation
        fields = ['formation', 'date_debut', 'date_fin', 'niveau'] 

        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }