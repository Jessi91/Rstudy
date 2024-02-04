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
    print(request.GET.get('matiere'))
    if request.GET.get('Matiere:'):
        print(request.GET)
        return redirect(f"quizApp/quiz/?matiere={request.GET.get('Matiere')}")
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



def get_quiz(request):
    try:
        print(request.GET)
        matiere_name = request.GET.get('matiere')
        print(f"Matière : {matiere_name}")  # Add this line for debugging
        question_objs = Question.objects.all()
        if matiere_name:
            question_objs = question_objs.filter(matiere__matiere_name__icontains=matiere_name)
        question_objs = list(question_objs)
        random.shuffle(question_objs)
        data = []
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "matiere": question_obj.matiere.matiere_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.get_answers(),
            })
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")

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
