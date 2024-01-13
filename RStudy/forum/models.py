from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Forum(models.Model):
    id_forum = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    ouvert = models.BooleanField(default=False)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='forums_crees')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ParticipationForum', related_name='forums_participes')
    
    def delete(self): 
        # Supprime les participations associées à ce forum
        self.participationforum_set.all().delete()
        super().delete()

class ParticipationForum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='participations')
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    contenu = models.CharField(max_length=1000)
