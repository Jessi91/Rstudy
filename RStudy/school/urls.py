from django.urls import path
from . import views

urlpatterns = [
    path('school/', views.school, name='school'),
]