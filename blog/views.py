from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	returnHttpResponse("Hello To you, you are at the polls!)
i