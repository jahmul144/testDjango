from django.shortcuts import render_to_response
import datetime
# Create your views here.

from .models import Question 

def index(request):
	now = datetime.datetime.now()
	return render_to_response('polls.html', {'current_date': now})	

def questions(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	return render_to_response('polls/index1.html', {'question_latest': latest_question_list})

