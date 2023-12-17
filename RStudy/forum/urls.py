from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('create/', create_forum, name='create_forum'),
    path('show', show, name='show_forum'),
    re_path(r'^(?P<id>[\w-]+)/$', forum_detail, name='forum_detail'), 
    re_path(r'^send_message/(?P<id>[\w-]+)/$', send_message , name='send_message'), 
    
    re_path(r'^edit/(?P<id>[\w-]+)/$', edit, name='edit_forum'),  
    re_path(r'^update/(?P<id>[\w-]+)/$', update, name='update_forum'),  
    re_path(r'^delete/(?P<id>[\w-]+)/$', delete, name='delete_forum'), 
    path('message/', send_message, name='send_message'),
]
