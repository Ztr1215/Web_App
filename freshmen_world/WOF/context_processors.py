from WOF.models import University, Course, StudentUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def university_courses(request):
	if request.user.is_authenticated:
 		student_user = StudentUser.objects.filter(user=request.user)[0]
 		student_university = student_user.university
 		uni_courses = list(Course.objects.filter(university=student_university))
	else:
		uni_courses = {}
	return {'university_courses' : uni_courses }




