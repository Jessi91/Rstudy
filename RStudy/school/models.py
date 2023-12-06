
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings
from user.models import User

# from RStudy.home.models import Enseignement, Matiere, MatiereFormation

from home.models import Enseignement, Matiere, MatiereFormation, Formation


# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/

class Formation(models.Model):
   
    @classmethod
    def create_formation(cls, _nom, _description, _type, _duree_mois, _responsable):
        formation = cls.objects.create(_nom=_nom, _description=_description, _type=_type, _duree_mois=_duree_mois, _responsable=_responsable)
        return formation

    @classmethod
    def add_matiere(cls, nom_matiere, description_matiere, duree_matiere, autres_informations):
        matiere = Matiere(_nom=nom_matiere, _description=description_matiere, _duree=duree_matiere, _autres_informations=autres_informations)
        matiere.save()
        MatiereFormation.objects.create(_formation=cls, _matiere=matiere, _ects=1)

    @classmethod
    def assign_enseignant(cls, professeur, matiere, groupe_td=None):
        enseignement = Enseignement.objects.create(_professeur=professeur, _matiere=matiere, _groupe_td=groupe_td)
        return enseignement


class EspacePersonnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dashboard = models.TextField(blank=True, null=True)
    calendrier = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    # Ajoutez d'autres champs selon vos besoins



class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    createur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

