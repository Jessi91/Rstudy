from django.urls import path
from school import views

urlpatterns = [
    path('school/', views.school, name='school'),
    path('test/', views.test_view, name='test_view'),
    path('espace_personnel/',views.espace_personnel, name='espace_personnel'),
    
]