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
                return redirect('succes')
            else:
                message = 'Les informations invalides.'
    return render(
  request, 'user/login.html', context={'form': form, 'message': message})

@login_required
def reussi(request) :
    return render(request, 'user/reussi.html')
