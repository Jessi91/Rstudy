from django.db import models 
import uuid 
import random 
from django.contrib.auth import get_user_model
from home.models import Matiere

User = get_user_model()

class BaseModel(models.Model): 
	uid = models.UUIDField(primary_key=True, 
						default=uuid.uuid4, editable=True) 
	created_at = models.DateField(auto_now_add=True) 
	updated_at = models.DateField(auto_now=True) 
	
	class Meta: 
		abstract = True


class Question(BaseModel):
    matiere = models.ForeignKey(Matiere, related_name='questions', on_delete=models.CASCADE)  # Changement ici
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)
        for answer_obj in answer_objs:
            data.append({
                'answer': answer_obj.answer,
                'is_correct': answer_obj.is_correct
            })
        return data


class Answer(BaseModel): 
	question = models.ForeignKey(Question, 
								related_name='question_answer', 
								on_delete=models.CASCADE) 
	answer = models.CharField(max_length=100) 
	is_correct = models.BooleanField(default=False) 
	
	def __str__(self) -> str: 
		return self.answer 

class Task(models.Model):
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title