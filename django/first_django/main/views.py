
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic



# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
	model = Question
	template_name = 'polls/result.html'
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST["choice"])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, "polls/detail.html", {"error_message":"You didn't select a choice", "question": question})
	else:
		selected_choice.votes = F("votes") + 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))