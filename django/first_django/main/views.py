
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.shortcuts import render,get_object_or_404



# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = "".join([q.question_text for q in latest_question_list])
    context = {
    	"latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)



def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html",{"question": question})
	


def result(request, question_id):
	response = "You are looking results for question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	response = "You're voting for question %s"
	return HttpResponse(response % question_id)