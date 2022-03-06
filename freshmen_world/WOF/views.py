from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	context_dict = {}
	response = render(request, 'WOF/index.html', context=context_dict)
	return response

def login(request):
	context_dict = {}
	response = render(request, 'WOF/user_login.html', context=context_dict)
	return response
