from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {}
	response = render(request, 'WOF/index.html', context=context_dict)
	return response

def base(request):
	return render(request, 'WOF/base.html', context={})

def user_login(request):
	context_dict = {}
	response = render(request, 'WOF/login.html', context=context_dict)
	return response

def user_register(request):
	context_dict = {}
	response = render(request, 'WOF/register.html', context=context_dict)
	return response

def selector(request):
	context_dict = {}
	response = render(request, 'WOF/selecting.html', context=context_dict)
	return response

def task_manager(request):
	context_dict = {}
	response = render(request, 'WOF/taskmanager.html', context=context_dict)
	return response

