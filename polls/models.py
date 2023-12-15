from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_txt = models.CharField("Pergunta", max_length = 200)
    pub_date = models.DateField("Data")

    def __str__(self):
        return self.question_txt
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField("Insira a resposta", max_length= 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_txt
