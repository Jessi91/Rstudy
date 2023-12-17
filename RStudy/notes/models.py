from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model 

from django.conf import settings

from django.utils.timezone import now

class Note(models.Model):
    title = models.CharField(max_length=950, blank=True, null=True)
    users = models.ManyToManyField(to=get_user_model(), through='Setting')
    contents = models.ManyToManyField('Content', related_name='notes', blank=True)
    images = models.ManyToManyField('Image', related_name='notes', blank=True)
    reminder = models.OneToOneField(
        'Reminder', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='+'
    )
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      # Ajouté

    def __str__(self):
        return f'Note {self.pk}'

class Label(models.Model):
    text = models.CharField(max_length=150)
    notes = models.ManyToManyField('Note', related_name='labels', blank=True)

    def __str__(self):
        return ' Label ' + str(self.pk)
  


class Setting(models.Model):
    white = 'W'
    red = 'R'
    blue = 'B'
    green = 'G'
    yellow = 'Y'
    pink = 'P'
    violet = 'V'
    COLORS = (
        (white, 'White'),
        (red, 'Red'),
        (blue, 'Blue'),
        (green, 'Green'),
        (yellow, 'Yellow'),
        (pink, 'Pink'),
        (violet, 'Violet'),
    )
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=1, choices=COLORS, default=white)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    labels = models.ManyToManyField(to=Label, through='SettingLabel', blank=True)
    trash_delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('order', 'pk')
        unique_together = ('user', 'note')

    def __str__(self):
        return 'Setting: note ' + str(self.note.id) + ', user ' + str(self.user.id)


class SettingLabel(models.Model):
    label = models.ForeignKey(to=Label, on_delete=models.CASCADE)
    setting = models.ForeignKey(to=Setting, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('label', 'setting')

    def __str__(self):
        return 'Setting Label: setting ' + str(self.setting.id) + ', label ' + str(self.label.id)


class Content(models.Model):
    done = 'T'
    not_done = 'F'
    hidden = 'H'

    STATUS_CHOICES = (
        (hidden, 'Hidden'),
        (done, 'Done'),
        (not_done, 'Not Done'),
    )

    order = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=hidden)
    text = models.CharField(max_length=950)
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE)

    class Meta:
        ordering = ('order', 'pk')

    def __str__(self):
        return 'Content: ' + str(self.note) + ', Item ' + str(self.pk)


class Image(models.Model):
    image = models.ImageField(upload_to='note_images')
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.note) + ' Image ' + str(self.pk)


class Reminder(models.Model):
    no_repeat = 'N'
    daily = 'D'
    weekly = 'W'
    monthly = 'M'
    yearly = 'Y'
    REPEAT_CHOICES = (
        (no_repeat, 'Does Not Repeat'),
        (daily, 'Daily'),
        (weekly, 'Weekly'),
        (monthly, 'Monthly'),
        (yearly, 'Yearly'),
    )
    date_and_time = models.DateTimeField(default=timezone.now)
    # TODO: add costume repeat schedule
    repeat = models.CharField(max_length=1, choices=REPEAT_CHOICES, default=no_repeat)
    note = models.OneToOneField(
        'Note', 
        on_delete=models.CASCADE, 
        related_name='+'
    )
    def __str__(self):
        return str(self.note) + ' Reminder ' + str(self.pk)