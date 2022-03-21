from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from WOF.forms import StudentUserForm, StudentUserProfileForm


def index(request):
	context_dict = {}
	response = render(request, 'WOF/index.html', context=context_dict)
	return response

def base(request):
	return render(request, 'WOF/base.html', context={})

def team_members(request):
	return render(request, 'WOF/team_members.html', context={})

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
		return render(request, 'WOF/user_login.html')
	return response

def user_register(request):
	registered = False

	if request.method == "POST":
		student_user_form = StudentUserForm(request.POST)
		student_user_profile_form = StudentUserProfileForm(request.POST)

		if student_user_form.is_valid() and student_user_profile_form.is_valid():
			student_user = student_user_form.save()
			student_user.set_password(student_user.password)
			student_user.save()

			profile = student_user_profile_form.save(commit=False)
			profile.user = student_user

			profile.save()

			registered = True
		else:
			print(student_user_form.errors)
	else:
		student_user_form = StudentUserForm()
		student_user_profile_form = StudentUserProfileForm()
	return render(request, 'WOF/user_register.html', context={'student_user_form': student_user_form, 
														'student_user_profile_form': student_user_profile_form,
															'registered': registered})

@login_required
def user_logout(request):
	logout(request)
	return redirect(reverse('WOF:index'))

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
