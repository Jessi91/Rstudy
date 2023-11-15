from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),

]


urlpatterns = [
    path('creer_groupe/', views.creer_groupe, name='creer_groupe'),
    path('liste_groupes/', views.liste_groupes, name='liste_groupes'),
    path('inviter_amis/<int:groupe_id>/', views.inviter_amis, name='inviter_amis'),
]

