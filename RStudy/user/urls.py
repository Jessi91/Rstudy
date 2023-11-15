from django.contrib.auth.views import LoginView
from django.urls import path, include
import user.views
urlpatterns = [
   path('signup/', user.views.signup_page, name='signup'),
    path('login/', user.views.login_page, name='login'),
    path('succes/', user.views.reussi, name='succes'),
    path('profil/', user.views.readProfile, name='profile'),
    path('update/', user.views.update_profile, name='update_profile'),
]