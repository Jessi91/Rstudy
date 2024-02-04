from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib.auth.views import LogoutView
import user.views
urlpatterns = [
   path('signup/', user.views.signup_page, name='signup'),
    path('login/', user.views.login_page, name='login'),
    path('succes/', user.views.reussi, name='succes'),
    path('profile/', user.views.readProfile, name='profile'),
    path('update/', user.views.update_profile, name='update_profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('inscription-formation/', user.views.inscription_formation, name='inscription_formation'),
    path('liste_matiere/', user.views.liste_matiere, name='liste_matiere'),
    
]