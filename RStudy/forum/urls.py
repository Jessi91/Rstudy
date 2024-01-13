from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('create/', create_forum, name='create_forum'),
    path('show', show, name='show_forum'),
    re_path(r'^(?P<id>[\w-]+)/$', forum_detail, name='forum_detail'), 
    re_path(r'^edit/(?P<id>[\w-]+)/$',update, name='edit_forum'),  
    re_path(r'^delete/(?P<id>[\w-]+)/$', delete, name='delete_forum'),
    path('send_message/<uuid:id_forum>/', send_message, name='send_message'),
]
