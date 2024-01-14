from django.db import models
from django.contrib.auth import get_user_model

class PomodoroSession(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
