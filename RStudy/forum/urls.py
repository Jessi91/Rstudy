from django.urls import path, re_path
from . import views  

urlpatterns = [
    path('create/', views.create_forum, name='create_forum'),
    path('show', views.show, name='show_forum'),  
    re_path(r'^edit/(?P<id>[\w-]+)/$', views.edit, name='edit_forum'),  
    re_path(r'^update/(?P<id>[\w-]+)/$', views.update, name='update_forum'),  
    re_path(r'^delete/(?P<id>[\w-]+)/$', views.delete, name='delete_forum'), 
    # Messages
    path("", views.messages_page),
]
