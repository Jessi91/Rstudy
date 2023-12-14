from django.contrib import admin

from .models import *

admin.site.register(Note)
admin.site.register(Setting)
admin.site.register(SettingLabel)
admin.site.register(Reminder)
admin.site.register(Image)
admin.site.register(Content)
admin.site.register(Label)