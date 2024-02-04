from django.db import models
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
    def __str__(self):
        return self.nom

    
    
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
    duree = models.IntegerField()
    autres_informations = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.nom

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
    
    class Meta:
        # Définir une contrainte d'unicité sur la combinaison de 'formation' et 'matiere'
        unique_together = ('formation', 'matiere')

    def __str__(self):
        return f"{self.formation.nom} - {self.matiere.nom}"


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
        MembresGroupe.objects.create(user=user, groupe=self)

    @property
    def get_nom_groupe(self):
        return self.nom_groupe



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
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    contenu = models.CharField(max_length=255, blank=True, null=True)
    
class Invitation(models.Model):
    groupe = models.ForeignKey(GroupeEtude, on_delete=models.CASCADE)
    invitant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invitations_envoyees')
    invite = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invitations_recues')
    statut = models.CharField(max_length=20, choices=[('en_attente', 'En attente'), ('accepte', 'Accepté'), ('refuse', 'Refusé')])

    # Ajoutez un champ pour le rôle dans le groupe
    droit_acces = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('contributor', 'Contributor'), ('lecteur', 'Lecteur')])

