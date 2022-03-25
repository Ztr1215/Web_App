from WOF.models import University, Course, StudentUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def university_courses(request):
	if request.user.is_authenticated and StudentUser.objects.filter(user=request.user).exists():
		student_user = StudentUser.objects.filter(user=request.user)[0]
		if student_user.university != None:
			student_university = student_user.university
			uni_courses = list(Course.objects.filter(university=student_university))
		else:
			uni_courses = {}
	else:
		uni_courses = {}
	return {'university_courses' : uni_courses }


def university_options(request):
	context_dict = {}
	uni_options = University.objects.all()
	context_dict['universities'] = uni_options
	return context_dict

def check_admin(request):
	# User is logged in and student user exists
	if request.user.is_authenticated and StudentUser.objects.filter(user=request.user).exists():
		student_user = StudentUser.objects.filter(user=request.user)[0]
		# Student User has admin field
		if student_user.isAdmin != None:
			# Student user is admin
			if student_user.isAdmin == True:
				return {'is_admin' : True}
	return {'is_admin' : False}

def check_university(request):
	if request.user.is_authenticated and StudentUser.objects.filter(user=request.user).exists():
		student_user = StudentUser.objects.filter(user=request.user)[0]
		if student_user.university != None:
			if student_user.university in list(University.objects.all()):
		 		return {'student_university' : True}
	return {'student_university' : False}


