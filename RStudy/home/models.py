from django.db import models

# Create your models here.
# https://docs.djangoproject.com/fr/4.2/topics/db/models/#field-types
# https://docs.djangoproject.com/fr/4.2/intro/tutorial02/

class Etablissement(models.Model):
    siren = models.BigAutoField(primary_key=True)
    denomination = models.CharField(max_length=200 )
    numtva = models.CharField(max_length=13 )
    activite_principale = models.CharField(max_length = 100 )
    naf = models.CharField(max_length= 5)
    adresse = models.CharField(max_length=200 )
    nature_juridique = models.CharField(max_length=200 )
    effectif_salarie =  models.IntegerField()
    date_naissance = models.DateTimeField("date de création")
    convention = models.CharField(max_length=200)

     

class Medecin(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50 )
    nom = models.CharField(max_length=50)
    sexe = [
        ("F", "Feminin"),
        ("M", "Masculin"),
        ("O", "Other"),
    ]
    date_naissance = models.DateTimeField("date de naissance")
    adresse = models.CharField(max_length=200 )

    # Numero de tel français pour l'instant
    numtel = models.IntegerField()
    adresse_mail = models.EmailField()
    
    # Le numéro RPPS 11 chiffres
    numlicence = models.IntegerField()
    horaires = models.CharField(max_length=200 )
    agenda = models.URLField()
    photo = models.CharField(max_length=200 )
    accept_mutuel = models.BooleanField()
    specialite = models.CharField(max_length=50)
    etablissement = models.ForeignKey(Etablissement, blank=True, default= 0000, on_delete=models.PROTECT )

class Patient(models.Model):
    num_secu = models.IntegerField(primary_key=True )
    nom = models.CharField(max_length=50 )
    nom = models.CharField(max_length=50)
    sexe = [
        ("F", "Feminin"),
        ("M", "Masculin"),
        ("O", "Other"),
    ]
    date_naissance = models.DateTimeField("date de naissance")
    adresse = models.CharField(max_length=200 )
    # Numero de tel français pour l'instant
    numtel = models.IntegerField()
    adresse_mail = models.EmailField()
    # Le numéro RPPS 11 chiffres
    pathologie = models.CharField(max_length=200)
    mutuelle = models.CharField(max_length=200)

class Rendezvous(models.Model) :
    id = models.BigAutoField(primary_key=True)
    date= models.DateField
    heure = models.DateTimeField
    premiere_consult = models.BooleanField
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE )
