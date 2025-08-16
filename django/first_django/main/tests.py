from django.test import TestCase
import datetime
from django.utils import timezone
from sqlalchemy.testing import future

from .models import Question, Choice
from django.urls import reverse

# Create your tests here.
def create_question(question_text, days):
    """
        Create a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)



class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for questions whose pub_date is in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        return self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        return self.assertIs(recent_question.was_published_recently(), True)

    def test_does_question_has_choices(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        question = Question.objects.create(question_text="What are you doing today?", pub_date=time)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context['latest_question_list'], [])





class QuestionIndexViewTest(TestCase):
    """If no question exist, an appropriate message is displayed."""
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        """
                Questions with a pub_date in the past are displayed on the
                index page.
                """
        question = create_question('Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question])

    def test_future_questions(self):
        """
                Questions with a pub_date in the future aren't displayed on
                the index page.
                """
        question = create_question('Future question', days=30)
        choice = Choice.objects.create(question=question, choice_text='Choose one', votes=0)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])


    def test_future_question_and_past_question(self):
        """
                Even if both past and future questions exist, only past questions
                are displayed.
                """
        question = create_question('Past question', days=-30)
        create_question(question_text='Future question', days=30)
        choice = Choice.objects.create(question=question, choice_text='Choose one', votes=0)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question])

    def test_two_past_questions(self):
        question1 = create_question('Past question 1', days=-30)
        question2 =create_question('Past question 2', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question1, question2, ])


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question('Future question', days=30)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """ The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question('Past question', days=-30)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)

class QuestionResultsViewTest(TestCase):
    def test_future_question(self):
        "If the question is in the future, do not show it"
        future_question = create_question('Future question', days=30)
        response = self.client.get(reverse('polls:result', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        "If the question is in the past, do  show it"
        past_question = create_question('Past question', days=-30)
        response = self.client.get(reverse('polls:result', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)










