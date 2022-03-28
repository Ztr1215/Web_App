from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from WOF.forms import *
from WOF.models import StudentUser, Course, University
from WOF.xmlWriter import writeCourseToXML, writeUniversityToXML
import xml.etree.ElementTree as ET, os, datetime as datetime

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
	student_user_university = None
	if (StudentUser.objects.filter(user=request.user).exists()):
		student_user = StudentUser.objects.filter(user=request.user)[0]
		if student_user.university != None:
			student_user_university = student_user.university
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
														'student_user_university' : student_user_university,
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

@login_required
def delete_course(request, course_name_slug):
	if request.method == "POST" and Course.objects.filter(slug=course_name_slug).exists():
		course = Course.objects.filter(slug=course_name_slug)[0]
		name_of_deleted = course.name
		course.delete()
		return file_deleted(request, name_of_deleted)
	else:
		return error(request, f"Failed to delete course with slug {course_name_slug}")

@login_required
@csrf_exempt
def delete_university(request):
	if request.is_ajax and request.method == "POST":
		print("okay")
		university_name_slug = request.POST.get('university_slug')
		if University.objects.filter(slug=university_name_slug).exists():
			print("deleting task ongoing")
			uni_deleted = University.objects.filter(slug=university_name_slug)[0]
			name_of_deleted = uni_deleted.name
			uni_deleted.delete()
		else:
			error(request, "University not found")
	return profile(request)

def add_university(request):
	university_created = False
	university = None
	if request.method == "POST":
		university_form = UniversityForm(request.POST)
		if university_form.is_valid() and StudentUser.objects.filter(user=request.user)[0].isAdmin:
			university = university_form.save()
			student_user = StudentUser.objects.filter(user=request.user)[0]

			# writeUniversityToXML
			writeUniversityToXML(university.slug)
			student_user.university = university
			student_user.uni_admin = university
			student_user.save()
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
	if University.objects.filter(slug=university_name_slug).exists():
		university = University.objects.filter(slug=university_name_slug)[0]
		courses = list(Course.objects.filter(university=university))
		context_dict['university'] = university
		context_dict['courses'] = courses
		return render(request, 'WOF/university_base.html', context=context_dict)
	else:
		return error(request, f"University at: {university_name_slug} does not exist")

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
					print(information)
					return JsonResponse({ 'course_text' : information })
		return JsonResponse({})
	else:
		return JsonResponse({})


arrayNums = [x for x in range(1,13)]
months = ["January", "Febuary", "March", "April", "May", "June", 
		"July", "August", "September", "October", "November", "December"];

all_months = dict(zip(months, arrayNums))

# HELPER FUNCTION NOT VIEW
def find_days_in_month(month : int, year : int):
	monthNum = month
	nextMonthNum = (monthNum + 1) % 12
	nextMonth = int(arrayNums[nextMonthNum-1])
	nextYear = year if nextMonth != 1 else year + 1 
	return abs((datetime.datetime(nextYear, nextMonth, 1) - datetime.datetime(year, monthNum, 1)).days)

@csrf_exempt
def find_tasks_month(request):
	if request.is_ajax and request.method == "POST":
		if StudentUser.objects.filter(user=request.user).exists():
			student_user = StudentUser.objects.filter(user=request.user)[0]
			month = int(request.POST.get("month")) + 1
			year = int(request.POST.get("year"))
			# Finding time between each month
			daysInMonth = find_days_in_month(month, year)
			tasks = {}
			for i in range(1, daysInMonth+1):
				date = datetime.datetime(year, month, i)
				if Task.objects.filter(dueDate=date).exists():
					tasks[i] = str(Task.objects.get(dueDate=date))

			return JsonResponse({"tasks" : tasks})
		else:
			return JsonResponse({"tasks" : []})
	else:
		return error(request, "Error occurred while searching database")

def check_task_exists(task_name, dueDate):
	slug_name = slugify(task_name)+f"-{dueDate.year}-{dueDate.month}-{dueDate.day}"
	return (Task.objects.filter(slug=slug_name)).exists()

@csrf_exempt
def add_task(request):
	if request.is_ajax and request.method == "POST":
		if request.user.is_authenticated and StudentUser.objects.filter(user=request.user).exists():
			student_user = StudentUser.objects.filter(user=request.user)[0]
			task_name = request.POST.get('task_name')
			day = request.POST.get('day')
			month = request.POST.get('month')
			year = request.POST.get('year')
			response_data = {}
			actualMonth = all_months[month]

			date_created = datetime.datetime(int(year), int(actualMonth), int(day))
			if (check_task_exists(task_name, date_created)):
				return JsonResponse({"result": "Task already exists"})
			created_task = Task.objects.create(name=task_name, dueDate=date_created, studentUser=student_user)
			created_task.save()

			response_data['result'] = "success"
			response_data['user'] = str(student_user)
			return JsonResponse(response_data, status=200)
		elif not request.user.is_authenticated:
			return error(request, "Must be logged in to make a task")
	return error(request, "Database search failure")

def task_manager(request):
	context_dict = {}
	response = render(request, 'WOF/taskmanager.html', context=context_dict)
	return response
 

def error(request, error_message="No error/unknown error"):
	context_dict = {}
	context_dict['error'] = error_message
	return render(request, 'WOF/error_page.html', context=context_dict)


def file_deleted(request, file_name="File name not found"):
	context_dict = {}
	context_dict['file_deleted'] = file_name
	return render(request, 'WOF/deleted_file.html', context=context_dict)
