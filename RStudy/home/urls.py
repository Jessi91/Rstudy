from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .views import accepter_invitation, refuser_invitation


urlpatterns = [
    path('creer_groupe/', views.creer_groupe, name='creer_groupe'),
    path('liste_groupes/', views.liste_groupes, name='liste_groupes'),  
    re_path(r'^inviter_amis/(?P<id>[\w-]+)/$',views.inviter_amis, name='inviter_amis'),
    path('', views.index, name="home"),
    re_path(r'^accepter_invitation/(?P<id>[\w-]+)/$', accepter_invitation, name='accepter_invitation'),
    re_path(r'^refuser_invitation/(?P<id>[\w-]+)/$', refuser_invitation, name='refuser_invitation'),
]

