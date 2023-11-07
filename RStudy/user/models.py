from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('etudiant', 'Etudiant'),
        ('tuteur', 'Tuteur'),
        ('enseignant', 'Enseignant'),
    )

    # _id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # _nom = models.CharField(max_length=255)
    # _prenom = models.CharField(max_length=255)
    _sexe_f = models.BooleanField(blank=True, null=True)
    _date_naissance = models.DateField()
    _adresse = models.CharField(max_length=255)
    _num_tel = models.IntegerField(blank=True, null=True, unique=True)
    _adresse_mail = models.EmailField(max_length=255, unique=True)
    # _mot_de_passe = models.
    _role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    username = None
    
    # @property
    # def  get_id_user(self):
    #     return self._id_user

#     # @property
    # def  get_nom(self):
#     #     return self._nom

#     # @property
    # def  get_prenom(self):
#     #     return self._prenom

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
    def  get_adresse_mail(self):
        return self._adresse_mail

    @property
    def  get_role(self):
        return self._role

    USERNAME_FIELD = '_adresse_mail'
    REQUIRED_FIELDS = []
    objects = UserManager()
