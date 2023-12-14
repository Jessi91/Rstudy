from rest_framework import permissions

from .models import *


class HasNotePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        setting = Setting.objects.filter(user_id=request.user.id, note_id=view.kwargs['pk']).exists()
        return setting


class HasLabelPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        setting_label = SettingLabel.objects.filter(setting__user_id=request.user.id, label_id=obj).exists()
        return setting_label


class NoteIsNotInTrashPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        setting = Setting.objects.filter(user_id=request.user.id, note_id=obj, trash_delete_time=None).exists()
        return setting


class NoteIsNotArchivedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        setting = Setting.objects.filter(user_id=request.user.id, note_id=obj, is_archived=False).exists()
        return setting