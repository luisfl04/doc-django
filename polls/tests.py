from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question


class QuestionModelTest(TestCase):

    def test_de_valor(self):
        valor_de_teste = Question("10")
        self.assertIs(valor_de_teste.teste(), True)
