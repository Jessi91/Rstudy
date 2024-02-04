from django import forms
from .models import Task, Question, Answer

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'details','start_datetime', 'end_datetime']

        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['matiere', 'question', 'marks']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'answer', 'is_correct']