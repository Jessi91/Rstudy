# Generated by Django 4.2.5 on 2023-12-02 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='participationforum',
            name='_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membresgroupe',
            name='_groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.groupeetude'),
        ),
        migrations.AddField(
            model_name='membresgroupe',
            name='_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matiereformation',
            name='_formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.formation'),
        ),
        migrations.AddField(
            model_name='matiereformation',
            name='_matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.matiere'),
        ),
        migrations.AddField(
            model_name='formation',
            name='_responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enseignement',
            name='_matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.matiere'),
        ),
        migrations.AddField(
            model_name='enseignement',
            name='_professeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enregistrementformation',
            name='_formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.formation'),
        ),
        migrations.AddField(
            model_name='enregistrementformation',
            name='_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
