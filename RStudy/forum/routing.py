from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('forum/', consumers.ChatConsumer.as_asgi()),
]