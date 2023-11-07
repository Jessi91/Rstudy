# Generated by Django 4.2.5 on 2023-11-07 19:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_titre', models.CharField(max_length=255)),
                ('_description', models.CharField(blank=True, max_length=255, null=True)),
                ('_date_add', models.DateField(auto_now_add=True)),
                ('_path', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='EnregistrementFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_date_debut', models.DateField()),
                ('_date_fin', models.DateField(blank=True, null=True)),
                ('_niveau', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_groupe_td', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('_id_formation', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_nom', models.CharField(max_length=255)),
                ('_description', models.CharField(blank=True, max_length=255, null=True)),
                ('_type', models.CharField(choices=[('licence', 'Licence'), ('Master', 'Master'), ('Doctorat', 'Doctorat'), ('BTS', 'BTS'), ('DUT', 'DUT'), ('CPGE', 'CPGE'), ('Formation professionnelle', 'Formation professionnelle'), ('Autre', 'Autre')], max_length=255)),
                ('_duree_mois', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_nom', models.CharField(max_length=255)),
                ('_description', models.CharField(max_length=255)),
                ('_ouvert', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroupeEtude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_nom_groupe', models.CharField(max_length=255)),
                ('_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('_id_matiere', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_nom', models.CharField(max_length=255)),
                ('_description', models.CharField(blank=True, max_length=255, null=True)),
                ('_duree', models.TimeField()),
                ('_autres_informations', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatiereFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_ects', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MembresGroupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_date_ajout', models.DateTimeField(auto_now_add=True)),
                ('_role_groupe', models.CharField(choices=[('admin', 'Administrateur'), ('lecteur', 'Lecteur'), ('user', 'User')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_description', models.CharField(blank=True, max_length=255, null=True)),
                ('_type', models.CharField(max_length=255)),
                ('_contenu', models.CharField(blank=True, max_length=255, null=True)),
                ('_matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_date', models.DateTimeField(auto_now_add=True)),
                ('_titre_msg', models.CharField(max_length=255)),
                ('_contenu', models.CharField(max_length=255)),
                ('_forum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.forum')),
            ],
        ),
    ]
