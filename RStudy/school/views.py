from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def school(request):
    template = loader.get_template('school/first.html')
    return HttpResponse(template.render())

# def index(request):
#     return render(request, 'home/index.html')


