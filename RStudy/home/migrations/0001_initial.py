# Generated by Django 4.2.5 on 2023-11-22 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id_doc', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('path', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id_formation', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('licence', 'Licence'), ('Master', 'Master'), ('Doctorat', 'Doctorat'), ('BTS', 'BTS'), ('DUT', 'DUT'), ('CPGE', 'CPGE'), ('Formation professionnelle', 'Formation professionnelle'), ('Autre', 'Autre')], max_length=255)),
                ('duree_mois', models.IntegerField()),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id_forum', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('ouvert', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroupeEtude',
            fields=[
                ('id_group', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom_groupe', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id_matiere', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('duree', models.TimeField()),
                ('autres_informations', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(max_length=255)),
                ('contenu', models.CharField(blank=True, max_length=255, null=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipationForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('titre_msg', models.CharField(max_length=255)),
                ('contenu', models.CharField(max_length=255)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembresGroupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('role_groupe', models.CharField(choices=[('admin', 'Administrateur'), ('lecteur', 'Lecteur'), ('user', 'User')], max_length=255)),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.groupeetude')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MatiereFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ects', models.FloatField(default=1)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.formation')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe_td', models.IntegerField(blank=True, null=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.matiere')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EnregistrementFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('niveau', models.CharField(max_length=255)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.formation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
