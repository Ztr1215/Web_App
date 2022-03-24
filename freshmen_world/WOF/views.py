from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from WOF.forms import *
from WOF.models import StudentUser, Course, University
from WOF.xmlWriter import writeCourseToXML, writeUniversityToXML
import xml.etree.ElementTree as ET, os

def index(request):
	context_dict = {}
	response = render(request, 'WOF/index.html', context=context_dict)
	return response

def team_members(request):
	return render(request, 'WOF/team_members.html', context={})

def selector(request):
	return redirect(reverse("WOF:index"))

@login_required
def profile(request):
	updated = False
	if (StudentUser.objects.filter(user=request.user).exists()):
		student_user = StudentUser.objects.filter(user=request.user)[0]
	else:
		return redirect(reverse('WOF:index'))
	
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

	
@login_required
def show_course(request, course_name_slug):
	context_dict = {}
	try:
		course = Course.objects.filter(slug=course_name_slug)[0]
		context_dict['course'] = course
	except Course.DoesNotExist:
		context_dict['course'] = None
	return render(request, 'WOF/course_base.html', context=context_dict)

@login_required
def add_course(request):
	course_created = False
	course = None
	if request.method == "POST":
		course_form = CourseForm(request.POST)
		if course_form.is_valid():
			course = course_form.save()

			course_created = True
			# Make function to write to xml 
			writeCourseToXML(course.university.slug, 
						course.slug, 
						request.POST.get('courseDescription'))

		else:
			print(course_form.errors)
	else:
		course_form = CourseForm()
	return render(request, 'WOF/add_course.html', context={'course_form' : course_form,
															'course_created' : course_created,
															'course' : course})
def add_university(request):
	university_created = False
	university = None
	if request.method == "POST":
		university_form = UniversityForm(request.POST)
		if university_form.is_valid():
			university = university_form.save()

			# writeUniversityToXML
			writeUniversityToXML(university.slug)

			university_created = True
		else:
			print(university_form.errors)
	else:
		university_form = UniversityForm()
	return render(request, 'WOF/add_university.html', context={'university_form' : university_form,
																'university_created' : university_created,
																'university' : university})




def show_university(request, university_name_slug):
	context_dict = {}
	try:
		university = University.objects.filter(slug=university_name_slug)[0]
		courses = list(Course.objects.filter(university=university))
		context_dict['university'] = university
		context_dict['courses'] = courses
	except University.DoesNotExist:
		context_dict['university'] = None
		context_dict['courses'] = courses
	return render(request, 'WOF/university_base.html', context=context_dict)

def get_course_info(request, course_name_slug):
	if request.is_ajax and request.method == "GET":
		WORK_DIR = os.getcwd()
		file = ET.parse(os.path.join(WORK_DIR, "static", "xml", "uni_course_info.xml"))
		university_elements = list(file.getroot())
		# All the university elements
		for university in university_elements:
			courses = list(university)
			# Each course for each university
			for course in courses:
				# If found correct course
				if (course.attrib.get('id') == course_name_slug):
					information = course.text
					return JsonResponse(course.text, status=200, safe=False)
		return JsonResponse({}, status=400)
	else:
		return JsonResponse({}, status=400)

def task_manager(request):
	context_dict = {}
	response = render(request, 'WOF/taskmanager.html', context=context_dict)
	return response
 



