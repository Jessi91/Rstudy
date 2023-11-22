from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/


class User( AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('etudiant', 'Etudiant'),
        ('tuteur', 'Tuteur'),
        ('enseignant', 'Enseignant'),
    )
    
    username = None
    
    sexe_f = models.BooleanField(blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    adresse = models.CharField(max_length=255)
    num_tel = models.IntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
