from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from . import forms

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'user/signup.html', context={'form': form})

def login_page(request):
    form = forms.LoginForm()
    message = ''

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.email}! Vous êtes connecté.'
                return redirect('home')
            else:
                message = 'Les informations invalides.'
    return render(
  request, 'user/login.html', context={'form': form, 'message': message})

@login_required
def reussi(request) :
    return render(request, 'user/reussi.html')

@login_required
def readProfile(request):
    return render(request, 'user/profile.html', {'user': request.user})

@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        form = forms.ReadUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirigez l'utilisateur vers la page de profil mise à jour ou toute autre page souhaitée.
            return redirect('profile')
    else:
        form = forms.ReadUpdateForm(instance=user)

    return render(request, 'user/update_profil.html', {'form': form})



@login_required
def inscription_formation(request):
    if request.method == 'POST':
        form = forms.EnregistrementFormationForm(request.POST)
        if form.is_valid():
            enregistrement = form.save(commit=False)
            enregistrement.user = request.user  # Définir l'utilisateur actuellement connecté comme l'utilisateur de l'enregistrement
            enregistrement.save()
            return redirect('nom_de_l_url_après_inscription')  # Redirigez vers une page appropriée
    else:
        form = forms.EnregistrementFormationForm()
    return render(request, 'user/inscription_formation.html', {'form': form})