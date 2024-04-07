from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import PomodoroSession
from django.contrib.auth.decorators import login_required

@login_required
def start_pomodoro(request):
    PomodoroSession.objects.create(user=request.user)
    return redirect('pomodoro_timer')

@login_required
def stop_pomodoro(request, session_id):
    session = PomodoroSession.objects.get(id=session_id, user=request.user)
    session.end_time = now()
    session.is_completed = True
    session.save()
    return redirect('pomodoro_timer')

@login_required
def pomodoro_timer(request):
    sessions = PomodoroSession.objects.filter(user=request.user)
    return render(request, 'promodoro/pomodoro_timer.html', {'sessions': sessions})