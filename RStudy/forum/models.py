from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model as User

# Create your models here.
class Forum(models.Model):
    id_forum = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ouvert = models.BooleanField(default=False)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ParticipationForum')
    
    def delete(self) : 
        # Supprime les participations associées à ce forum
        self.participationforum_set.all().delete()
        super(Forum, self).delete()


# User -- Forum : (M;N)
class ParticipationForum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    titre_msg = models.CharField(max_length=255)
    contenu = models.CharField(max_length=255)