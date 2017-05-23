from django.shortcuts import render_to_response
import datetime
# Create your views here.

def index(request):
	now = datetime.datetime.now()
	return render_to_response('polls.html', {'current_date': now})	
