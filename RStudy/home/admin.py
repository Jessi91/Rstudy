from django.contrib import admin
from .models import *

class MatiereFormationAdmin(admin.ModelAdmin):
    list_display = ('formation', 'matiere', 'ects')  

admin.site.register(Matiere)
admin.site.register(Formation)
admin.site.register(EnregistrementFormation)
admin.site.register(MatiereFormation, MatiereFormationAdmin)