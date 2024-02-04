from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from .models import *
import random 



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
