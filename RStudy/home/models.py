from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model as User


# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/

class Formation(models.Model):
    FORMATION_CHOICES = (
        ('licence', 'Licence'),
        ('Master', 'Master'),
        ('Doctorat', 'Doctorat'),
        ('BTS', 'BTS'),
        ('DUT', 'DUT'),
        ('CPGE', 'CPGE'),
        ('Formation professionnelle', 'Formation professionnelle'),
        ('Autre', 'Autre')
    )

    id_formation = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, choices=FORMATION_CHOICES)
    duree_mois = models.IntegerField()
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    
    
# User -- Formation : (M;N)
class EnregistrementFormation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    formation = models.ForeignKey(Formation, on_delete=models.PROTECT)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    niveau = models.CharField(max_length=255)

class Matiere(models.Model):
    id_matiere = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    duree = models.TimeField()
    autres_informations = models.CharField(max_length=255, blank=True, null=True)

# Enseignement -- Matiere : (M;N)
class Enseignement(models.Model):
    professeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    groupe_td = models.IntegerField(blank=True, null=True)

    
# Formation -- Matiere : (M;N)
class MatiereFormation(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.PROTECT)
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    ects = models.FloatField(default=1)

    
class Forum(models.Model):
    id_forum = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ouvert = models.BooleanField(default=False)

# User -- Forum : (M;N)
class ParticipationForum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    titre_msg = models.CharField(max_length=255)
    contenu = models.CharField(max_length=255)

class Document(models.Model):
    id_doc = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_add = models.DateField(auto_now_add=True)
    path = models.FileField(upload_to='documents/')

    
class GroupeEtude(models.Model):
    id_group = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_groupe = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    @property
    def add_user(self, user):
        MembresGroupe.objects.create(user=user, groupe=self, role_groupe='user')


# User -- GroupeEtude : (M;N)
class MembresGroupe(models.Model):
    ROLE_GROUPES = (
        ('admin', 'Administrateur'),
        ('lecteur', 'Lecteur'),
        ('user', 'User'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    groupe = models.ForeignKey(GroupeEtude, on_delete=models.PROTECT)
    date_ajout = models.DateTimeField(auto_now_add=True)
    role_groupe = models.CharField(max_length=255, choices=ROLE_GROUPES)


    @property
    def add_user(self, user):
        MembresGroupe.objects.create(user=user, groupe=self, role_groupe='user')
    

    
class Ressource(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    contenu = models.CharField(max_length=255, blank=True, null=True)
