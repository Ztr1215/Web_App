from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

def index(request):
	context_dict = {}
	response = render(request, 'WOF/index.html', context=context_dict)
	return response

def base(request):
	return render(request, 'WOF/base.html', context={})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse('WOF:index'))
			else:
				return HttpResponse("Account disabled")
		else:
			print(f"Invalid login details supplied: {username}, {password}")
			return HttpResponse("Invalid login details supplied")
	else:
		return render(request, 'WOF/login.html')
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

# def submit_task(request):
#     context_dict = {}
#     if request.method == 'POST':
#     	response = render(request,'WOF/form.html',context = context_dict)
# 	return response
