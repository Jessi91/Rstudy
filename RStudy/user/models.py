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
    
    username = models.CharField(max_length=255)
    
    _sexe_f = models.BooleanField(blank=True, null=True)
    _date_naissance = models.DateField(blank=True, null=True)
    _adresse = models.CharField(max_length=255)
    _num_tel = models.IntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    _role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    @property
    def  get_sexe_f(self):
        return self._sexe_f
    
    @property
    def  get_date_naissance(self):
        return self._date_naissance
    
    @property
    def  get_adresse(self):
        return self._adresse

    @property
    def  get_num_tel(self):
        return self._num_tel

    @property
    def  get_role(self):
        return self._role
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
