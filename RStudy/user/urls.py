from django.contrib.auth.views import LoginView
from django.urls import path, include
import user.views
urlpatterns = [
    path('', LoginView.as_view(
            template_name='user/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', user.views.logout_user, name='logout'),
]