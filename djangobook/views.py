from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def current_datetime1(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})


def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

#offset comes from the regex data capture in urls.py
def hours_ahead(request, offset):
	offset = int(offset)
	hour_offset = offset
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	next_time = dt
	#locals() we pass the value of locals(), which will include all variables defined at that point in the function’s execution. 
	return render_to_response('hours_ahead.html', locals())
