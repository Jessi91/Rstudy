from rest_framework import serializers
from rest_framework import validators
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from .models import Content, Image, Label, Note, Reminder, Setting, SettingLabel
#from .models import *

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model






class LabelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # Récupérer note_pk du contexte de la vue
        note_pk = self.context['view'].kwargs.get('pk')
        setting = get_object_or_404(Setting, note=note_pk, user=self.context['request'].user, trash_delete_time=None)
        label = Label.objects.create(**validated_data)
        SettingLabel.objects.create(label=label, setting=setting)
        return label

    class Meta:
        model = Label
        fields = ('id', 'text',)


class SettingSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)
    is_owner = serializers.BooleanField(read_only=True)

    class Meta:
        model = Setting
        exclude = ('user', 'trash_delete_time', 'note')


class SettingCreateOnlySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), write_only=True)
    note = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(), write_only=True)

    class Meta:
        model = Setting
        fields = ('user', 'note', 'is_owner')
        validators = [validators.UniqueTogetherValidator(queryset=Setting.objects.all(), fields=['note', 'user'])]


class SettingLabelSerializer(serializers.ModelSerializer):
    label = LabelSerializer(read_only=True)
    setting = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        note_pk = self.context['view'].kwargs['pk']
        label_pk = self.context['view'].kwargs['label_pk']
        user = self.context['request'].user
        setting = get_object_or_404(Setting, note=note_pk, user=user, trash_delete_time=None)
        setting_label = SettingLabel.objects.create(label_id=label_pk, setting=setting)
        return setting_label

    def validate(self, attrs):
        user = self.context['request'].user
        note_pk = self.context['view'].kwargs['pk']
        label_pk = self.context['view'].kwargs['label_pk']

        setting_label = SettingLabel.objects.filter(setting__note_id=note_pk, label_id=label_pk, setting__user_id=user,
                                                    setting__trash_delete_time=None)

        if setting_label:
            raise ValidationError(_('The fields {label, setting} must make a unique set.'), code='unique')
        return attrs

    class Meta:
        model = SettingLabel
        fields = ('id', 'label', 'setting')

    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'note')

    image = serializers.ImageField(max_length=None, use_url=True)

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'date_and_time', 'repeat', 'note')

    date_and_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    repeat = serializers.ChoiceField(choices=Reminder.REPEAT_CHOICES)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'  # Ajustez les champs selon vos besoins

class NoteSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    reminder = ReminderSerializer(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'contents', 'users', 'images', 'reminder', 'created_at', 'updated_at']

