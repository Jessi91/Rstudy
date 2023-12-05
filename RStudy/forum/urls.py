from django.urls import path, re_path
from .views import create_forum, show, edit, delete, update

urlpatterns = [
    path('create/', create_forum, name='create_forum'),
    path('show', show, name='show_forum'),  
    re_path(r'^edit/(?P<id>[\w-]+)/$', edit, name='edit_forum'),  
    re_path(r'^update/(?P<id>[\w-]+)/$', update, name='update_forum'),  
    re_path(r'^delete/(?P<id>[\w-]+)/$', delete, name='delete_forum'), 
]
