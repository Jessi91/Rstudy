from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q

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

# Messages 

class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)