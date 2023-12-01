from django.db import models

class Question(models.Model):
    question_txt = models.CharField(max_lenght = 200)
    pub_date = models.DateField("Data publicada")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)


