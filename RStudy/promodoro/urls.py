from django.urls import path
from .views import pomodoro_timer, start_pomodoro, stop_pomodoro

urlpatterns = [
    path('pomodoro/', pomodoro_timer, name='pomodoro_timer'),
    path('pomodoro/start/', start_pomodoro, name='start_pomodoro'),
    path('pomodoro/stop/<int:session_id>/', stop_pomodoro, name='stop_pomodoro'),
]
