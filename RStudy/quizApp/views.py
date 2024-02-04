from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from home.models import Matiere, EnregistrementFormation, MatiereFormation
from .models import *
import random 
from .forms import TaskForm
from utils import space_google_url, connect_google_api
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required

def home(request):
    context = {'matieres': Matiere.objects.all()}
    if request.GET.get('matiere'):
        return redirect(f"quizApp/quiz/?matiere={request.GET.get('matiere')}")
    return render(request, 'quizApp/home.html', context)



# def quiz(request):
#     category = request.GET.get('category', 'DefaultCategory')  # DefaultCategory can be any default value you want
#     context = {'category': category}
#     return render(request, 'quizApp/quiz.html', context)
def quiz(request):
    context = {'matiere': request.GET.get('matiere')} 
    return render(request, 'quizApp/quiz.html', context) 


# def quiz(request, category=None):
#     context = {'category': category or 'DefaultCategory'}  
#     return render(request, 'quizApp/quiz.html', context)

from django.http import JsonResponse
from .models import Question

def get_quiz(request):
    try:
        print(request.GET)
        matiere_nom = request.GET.get('matiere')
        questions = Question.objects.filter(matiere__nom__icontains=matiere_nom).prefetch_related('question_answer')
        
        data = [{
            "uid": str(question.uid),
            "matiere": question.matiere.nom,
            "question": question.question,
            "marks": question.marks,
            "answers": question.get_answers(),
        } for question in questions]
        
        return JsonResponse({'status': True, 'data': data})
    except Exception as e:
        print(e)
        return JsonResponse({'status': False, 'error': str(e)}, status=500)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associez la tâche à l'utilisateur actuellement connecté
            task.save()

            # Générez le lien Google Calendar à partir des données de la tâche
            title = space_google_url(task.title)
            start_datetime = task.start_datetime.strftime("%Y%m%dT%H%M%S")
            end_datetime = task.end_datetime.strftime("%Y%m%dT%H%M%S")
            details =  space_google_url(task.details)
            location = "paris,%20france"

            google_calendar_link = f"https://www.google.com/calendar/render?action=TEMPLATE&text={title}&dates={start_datetime}/{end_datetime}&ctz=Europe/Paris&details={details}&location={location}"

            # Redirigez l'utilisateur vers le lien Google Calendar
            return redirect(google_calendar_link)

    else:
        form = TaskForm()

    return render(request, 'google-apis/save_date.html', {'form': form})

def display_user_calendar(request):
    service = connect_google_api()

    # Récupérez les événements du calendrier de l'utilisateur
    events = service.events().list(calendarId='primary', timeMin='2024-02-01T00:00:00Z', maxResults=10, singleEvents=True, orderBy='startTime').execute()
    user_events = events.get('items', [])

    context = {'user_events': user_events}
    return render(request, 'google-apis/calendar.html', context)
