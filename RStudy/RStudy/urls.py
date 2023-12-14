from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('forum/', include('forum.urls')),
    path('user-', include('user.urls')),
    path('chat/', include('chat.urls')),

]

