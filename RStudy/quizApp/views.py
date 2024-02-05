from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from .models import *
import random 
from .forms import *
from utils import space_google_url


def home(request):
    context = {'categories': Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"quizApp/quiz/?category={request.GET.get('category')}")
    return render(request, 'quizApp/home.html', context)


# def quiz(request):
#     category = request.GET.get('category', 'DefaultCategory')  # DefaultCategory can be any default value you want
#     context = {'category': category}
#     return render(request, 'quizApp/quiz.html', context)
def quiz(request): 
    context = {'category': request.GET.get('category')} 
    return render(request, 'quizApp/quiz.html', context) 

# def quiz(request, category=None):
#     context = {'category': category or 'DefaultCategory'}  
#     return render(request, 'quizApp/quiz.html', context)


def get_quiz(request):
    try:
        category_name = request.GET.get('category')
        print(f"Category Name: {category_name}")  # Add this line for debugging
        question_objs = Question.objects.all()
        if category_name:
            question_objs = question_objs.filter(category__category_name__icontains=category_name)
        question_objs = list(question_objs)
        random.shuffle(question_objs)
        data = []
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
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
    """Crée une nouvelle tâche et redirige vers Google Calendar pour la programmer."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            # Génère le lien Google Calendar
            title = space_google_url(task.title)
            start_datetime = task.start_datetime.strftime("%Y%m%dT%H%M%S")
            end_datetime = task.end_datetime.strftime("%Y%m%dT%H%M%S")
            details = space_google_url(task.details)
            google_calendar_link = f"https://www.google.com/calendar/render?action=TEMPLATE&text={title}&dates={start_datetime}/{end_datetime}&details={details}"
            return redirect(google_calendar_link)
    else:
        form = TaskForm()
    return render(request, 'google-apis/save_date.html', {'form': form})
