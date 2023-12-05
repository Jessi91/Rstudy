from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings


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

    _id_formation = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _nom = models.CharField(max_length=255)
    _description = models.CharField(max_length=255, blank=True, null=True)
    _type = models.CharField(max_length=255, choices=FORMATION_CHOICES)
    _duree_mois = models.IntegerField()
    _responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    @property
    def  get_id_formation(self):
        return self._id_formation

    @property
    def  get_nom(self):
        return self._nom

    @property
    def  get_description(self):
        return self._description

    @property
    def  get_type(self):
        return self._type

    @property
    def  get_duree_mois(self):
        return self._duree_mois

    @property
    def  get_responsable(self):
        return self._responsable
    

    @classmethod
    def create_formation(cls, _nom, _description, _type, _duree_mois, _responsable):
        formation = cls.objects.create(_nom=_nom, _description=_description, _type=_type, _duree_mois=_duree_mois, _responsable=_responsable)
        return formation

    @classmethod
    def add_matiere(cls, nom_matiere, description_matiere, duree_matiere, autres_informations):
        matiere = Matiere(_nom=nom_matiere, _description=description_matiere, _duree=duree_matiere, _autres_informations=autres_informations)
        matiere.save()

        # Utilisez la variable d'instance cls pour référencer la formation actuelle
        MatiereFormation.objects.create(_formation=cls.objects.first(), _matiere=matiere, _ects=1)

        
    @classmethod
    def assign_enseignant(cls, professeur, matiere, groupe_td=None):
        enseignement = Enseignement.objects.create(_professeur=professeur, _matiere=matiere, _groupe_td=groupe_td)
        return enseignement




# User -- Formation : (M;N)
class EnregistrementFormation(models.Model):
    _user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    _formation = models.ForeignKey(Formation, on_delete=models.PROTECT)
    _date_debut = models.DateField()
    _date_fin = models.DateField(blank=True, null=True)
    _niveau = models.CharField(max_length=255)

    @property
    def  get_user(self):
        return self._user

    @property
    def  get_formation(self):
        return self._formation

    @property
    def  get_date_debut(self):
        return self._date_debut

    @property
    def  get_date_fin(self):
        return self._date_fin

    @property
    def  get_niveau(self):
        return self._niveau


class Matiere(models.Model):
    _id_matiere = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _nom = models.CharField(max_length=255)
    _description = models.CharField(max_length=255, blank=True, null=True)
    _duree = models.TimeField()
    _autres_informations = models.CharField(max_length=255, blank=True, null=True)

    @property
    def  get_id_matiere(self):
        return self._id_matiere

    @property
    def  get_nom(self):
        return self._nom

    @property
    def  get_description(self):
        return self._description

    @property
    def  get_duree(self):
        return self._duree

    @property
    def  get_autres_informations(self):
        return self._autres_informations


# Enseignement -- Matiere : (M;N)
class Enseignement(models.Model):
    _professeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    _matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    _groupe_td = models.IntegerField(blank=True, null=True)

    @property
    def  get_professeur(self):
        return self._professeur

    @property
    def  get_matiere(self):
        return self._matiere

    @property
    def  get_groupe_td(self):
        return self._groupe_td


# Formation -- Matiere : (M;N)
class MatiereFormation(models.Model):
    _formation = models.ForeignKey(Formation, on_delete=models.PROTECT)
    _matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    _ects = models.FloatField(default=1)

    @property
    def  get_formation(self):
        return self._formation

    @property
    def  get_matiere(self):
        return self._matiere

    @property
    def  get_ects(self):
        return self._ects


class Forum(models.Model):
    _nom = models.CharField(max_length=255)
    _description = models.CharField(max_length=255)
    _ouvert = models.BooleanField(default=False)

    @property
    def  get_nom(self):
        return self._nom

    @property
    def  get_description(self):
        return self._description

    @property
    def  get_ouvert(self):
        return self._ouvert


# User -- Forum : (M;N)
class ParticipationForum(models.Model):
    _user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    _forum = models.ForeignKey(Forum, on_delete=models.PROTECT)
    _date = models.DateTimeField(auto_now_add=True)
    _titre_msg = models.CharField(max_length=255)
    _contenu = models.CharField(max_length=255)

    @property
    def  get_user(self):
        return self._user

    @property
    def  get_forum(self):
        return self._forum

    @property
    def  get_date(self):
        return self._date

    @property
    def  get_titre_msg(self):
        return self._titre_msg

    @property
    def  get_contenu(self):
        return self._contenu


class Document(models.Model):
    _titre = models.CharField(max_length=255)
    _description = models.CharField(max_length=255, blank=True, null=True)
    _date_add = models.DateField(auto_now_add=True)
    _path = models.FileField(upload_to='documents/')

    @property
    def  get_titre(self):
        return self._titre

    @property
    def  get_description(self):
        return self._description

    @property
    def  get_date_add(self):
        return self._date_add

    @property
    def  get_path(self):
        return self._path

class GroupeEtude(models.Model):
    _nom_groupe = models.CharField(max_length=255)
    _description = models.CharField(max_length=255, blank=True, null=True)

    @property
    def  get_nom_groupe(self):
        return self._nom_groupe

    @property
    def  get_description(self):
        return self._description


# User -- GroupeEtude : (M;N)
class MembresGroupe(models.Model):
    ROLE_GROUPES = (
        ('admin', 'Administrateur'),
        ('lecteur', 'Lecteur'),
        ('user', 'User'),
    )

    _user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    _groupe = models.ForeignKey(GroupeEtude, on_delete=models.PROTECT)
    _date_ajout = models.DateTimeField(auto_now_add=True)
    _role_groupe = models.CharField(max_length=255, choices=ROLE_GROUPES)

    @property
    def  get_user(self):
        return self._user

    @property
    def  get_groupe(self):
        return self._groupe

    @property
    def  get_date_ajout(self):
        return self._date_ajout

    @property
    def  get_role_groupe(self):
        return self._role_groupe


class Ressource(models.Model):
    _matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    _description = models.CharField(max_length=255, blank=True, null=True)
    _type = models.CharField(max_length=255)
    _contenu = models.CharField(max_length=255, blank=True, null=True)

    @property
    def  get_matiere(self):
        return self._matiere

    @property
    def  get_description(self):
        return self._description

    @property
    def  get_type(self):
        return self._type

    @property
    def  get_contenu(self):
        return self._contenu
