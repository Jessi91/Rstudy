from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('quizhome/', views.quizhome, name='quizhome'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/<str:category>/', views.quiz, name='quiz_with_category'),  # Ajoutez cette ligne
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
    path('creer-tache/', views.create_task, name='creer_tache'),
	
]
