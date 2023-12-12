from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question
from django.urls import reverse


class QuestionModelTest(TestCase):
    
    # Testando se o método "was_published_recently retorna a data atual."
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta( days = 1, seconds = 1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recently_question = Question(pub_date = time)
        self.assertIs(recently_question.was_published_recently(), True)

# Criando uma função que cria perguntas:
def create_question(question_txt, days):
    time = timezone.now() + datetime.timedelta(days = days) # tempo de dias deslocados
    return Question.objects.create(question_txt = question_txt, pub_date = time) # retornando questão e dia por parâmetro
    
# testando a questão criada:
class QuestionIndexViewTests(TestCase):
    # testando se não há questões:
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index")) # Pegando o template.
        self.assertEqual(response.status_code, 200) # status da pag "index".
        self.assertContains(response, "No polls are available") # verificando mensagem.
        self.assertQuerySetEqual(response.context["latest_question_list"], []) # passando contexto.
    
    # Testando questões do passado:
    def test_past_questions(self):
        question = create_question(question_txt = "What`s your name?", days = -30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], [question]
             )# passando o contexto relacionado com a questão que foi criada.

    # Testando uma questão futura(não é exibida):
    def test_future_question(self):
        create_question(question_txt = "i am in the future!", days = 30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available") # verificando mensagem.
        self.assertQuerySetEqual(
            response.context["latest_question_list"], [] 
        ) # passando contexto, sem nenhuma questão na lista.

    # teste para que somente perguntas no passado sejam exibidas(independente se existam pergutas no futuro):
    def test_future_and_past_questions(self):
        question = create_question(question_txt = "i am in the past", days = -30) # questão no passado.
        create_question(question_txt = "i am in the future", days = 30) # questao no futuro
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], [question]
        ) # Passando o contexto com a questão no passado.

    # testando se a pag exibi múltiplas perguntas:
    def test_two_past_questions(self):
        frist_question = create_question(question_txt = "i am the primary question!", days = -30)
        second_question = create_question(question_txt = "i am the second question!", days = -10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], [second_question, frist_question]
        ) # contexto com múltiplas perguntas.

#Teste da view "Detail":
class DetailViewTestsQuestion(TestCase):
    
    # Verificação de questões com datas futuras:
    def test_future_question(self):
        future_question= create_question(question_txt = "future question", days = 20)
        url = reverse("polls:detail", args = (future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # verificação para questões no passado:
    def test_past_question(self):
        past_question = create_question(question_txt = "i am of the past!", days = -2)
        url = reverse("polls:detail", args = (past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_txt)

# Testes para a view "results":

class ResultsViewTest(TestCase):

    #para questões futuras:
    def test_future_questions(self):
        future_question = create_question(question_txt = "i am of the future!", days = 30)
        url = reverse("polls:results", args = (future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # questões no passado ou recentes:
    def test_past_question(self):
        past_question  = create_question(question_txt = "i am of the past!", days = -3)
        url = reverse("polls:results", args = (past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_txt)        


