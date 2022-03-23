from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from WOF.forms import StudentUserForm, StudentUserProfileForm
from WOF.forms import StudentUserChangeForm, StudentUserChangeProfileForm
from WOF.models import StudentUser, Course


def index(request):
	context_dict = {}
	response = render(request, 'WOF/index.html', context=context_dict)
	return response

def base(request):
	return render(request, 'WOF/base.html', context={})

def team_members(request):
	return render(request, 'WOF/team_members.html', context={})

@login_required
def profile(request):
	updated = False
	student_user = StudentUser.objects.filter(user=request.user)[0]
	if request.method == "POST":
		student_user_change_form = StudentUserChangeForm(request.POST, instance=request.user)
		student_user_change_profile_form = StudentUserChangeProfileForm(request.POST, instance=student_user)

		if student_user_change_form.is_valid() and student_user_change_profile_form.is_valid():
			updated = True
			
			student_user = student_user_change_form.save()
			student_user.set_password(student_user.password)
			student_user.save()

			student_user_profile = student_user_change_profile_form.save()
			student_user_profile.user = student_user 
			student_user_profile.save()

			login(request, student_user)
		else:
			print(student_user_change_form.errors, student_user_change_profile_form.errors)
	else:
		student_user_change_form = StudentUserChangeForm(instance=request.user)
		student_user_change_profile_form = StudentUserChangeProfileForm(instance=student_user)
	return render(request, 'WOF/account.html', context={'student_user_change_form' : student_user_change_form,
														'student_user_change_profile_form' : student_user_change_profile_form,
														'updated' : updated})

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
			login(request, student_user)
		else:
			print(student_user_form.errors, student_user_profile_form.errors)
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

def show_course(request, course_name_slug):
	context_dict = {}
	try:
		course = Course.objects.filter(slug=course_name_slug)[0]
		context_dict['course'] = course
	except Course.DoesNotExist:
		context_dict['course'] = None
	return render(request, 'WOF/course_base.html', context=context_dict)


def task_manager(request):
	context_dict = {}
	response = render(request, 'WOF/taskmanager.html', context=context_dict)
	return response

# def submit_task(request):
#     context_dict = {}
#     if request.method == 'POST':
#     	response = render(request,'WOF/form.html',context = context_dict)
# 	return response
