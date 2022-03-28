from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from WOF.views import *
from WOF.models import *
from WOF.xmlWriter import writeUniversityToXML

class TestBasicNonLoginViews(TestCase):

	def setUp(self):
		self.client = Client()
		
		self.team_url = reverse('WOF:team')
		self.task_manager_url = reverse('WOF:task_manager')

		self.glasgow_uni = University.objects.create(name="University of Glasgow", location="Glasgow")
		self.glasgow_slug = 'university-of-glasgow'
		self.glasgow_uni_url = reverse('WOF:show_university', args=(self.glasgow_slug,))

		self.basic_course = Course.objects.create(university=self.glasgow_uni, 
			name="Basic course", level=1, credits=10, courseConvener="TestUser", courseNumber="TEST2012")
		self.basic_course_slug = 'basic-course'
		self.course_url = reverse("WOF:show_course", args=(self.basic_course_slug,))

	def test_team_members_request(self):
		response = self.client.get(self.team_url)

		self.assertTemplateUsed(response, 'WOF/team_members.html')

	def test_university_page(self):
		response = self.client.get(self.glasgow_uni_url)
		self.assertTemplateUsed(response, 'WOF/university_base.html')

	def test_task_manager_page(self):
		response = self.client.get(self.task_manager_url)
		self.assertTemplateUsed(response, 'WOF/taskmanager.html')

	def test_course_failure(self):
		response = self.client.get(self.course_url)
		self.assertRedirects(response, '/WOF/login/?next=/WOF/selector/course/'+self.basic_course_slug+'/')

class TestAuthenticationViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.login_url = reverse("WOF:user_login")
		self.logout_url = reverse("WOF:logout")
		self.register_url = reverse("WOF:user_register")

		self.user = User.objects.create(username="SamJackson")
		self.user.set_password("12345")
		self.user.save()

		self.university = University.objects.create(name="University of Tests", location="Test Land")

		self.student_user = StudentUser.objects.create(user=self.user)


	def test_login(self):
		response = self.client.post(self.login_url, {'username' : 'SamJackson', 'password' : '12345'})
		self.assertTrue(auth.get_user(self.client))

	def test_logout(self):
		response = self.client.post(self.login_url, {'username' : 'SamJackson', 'password' : '12345'})
		self.client.get(self.logout_url)
		user_logged_out = auth.get_user(self.client)
		is_user_anonymous = user_logged_out.is_anonymous
		self.assertTrue(is_user_anonymous)

	def test_register_page(self):
		response = self.client.post(self.register_url, {'username' : "TestUser", 'password' : '12345'})
		user_made = User.objects.get(username="TestUser")
		self.assertTrue(user_made and StudentUser.objects.get(user=user_made))

	def test_register_with_uni(self):
		response = self.client.post(self.register_url, {'username' : "TestUser", 
									'password' : '12345', 'university' : self.university.pk	})

		user_made = User.objects.get(username="TestUser")
		student_user_made = StudentUser.objects.get(user=user_made)
		self.assertEquals(self.university, student_user_made.university)

	def test_register_admin(self):
		response = self.client.post(self.register_url, {'username' : "TestUser", 
									'password' : '12345', 'isAdmin' : True })

		user_made = User.objects.get(username="TestUser")
		student_user_made = StudentUser.objects.get(user=user_made)
		self.assertEquals(True, student_user_made.isAdmin)



class TestAddingViews(TestCase):
	
	def setUp(self):
		self.client = Client()
		self.login_url = reverse("WOF:user_login")
		self.university_url = reverse("WOF:add_university")
		self.course_url = reverse("WOF:add_course")

		self.basic_admin_user = User.objects.create(username="admin")
		self.basic_admin_user.set_password("12345")
		self.basic_admin_user.save()

		self.admin_student = StudentUser.objects.create(user=self.basic_admin_user, isAdmin=True)
		self.admin_student.save()

		self.basic_non_admin_user = User.objects.create(username="normaluser")
		self.basic_non_admin_user.set_password("12345")
		self.basic_non_admin_user.save()

		self.basic_non_admin_student = StudentUser.objects.create(user=self.basic_non_admin_user, isAdmin=False)
		self.basic_non_admin_student.save()

		self.university = University.objects.create(name="Test University", location="Test Land")

	def test_admin_can_login(self):
		self.client.post(self.login_url, {'username' : "admin", 'password' : "12345"})
		self.assertEquals("admin", auth.get_user(self.client).username)

	def test_non_admin_can_login(self):
		self.client.post(self.login_url, {'username' : "normaluser", 'password' : "12345"})
		self.assertEquals("normaluser", auth.get_user(self.client).username)

	def test_admin_add_university(self):
		self.client.post(self.login_url, {'username' : "admin", 'password' : "12345"})
		response = self.client.post(self.university_url, {'name' : "Better University", 'location' : "Better Place"})

		self.assertTrue(University.objects.get(slug="better-university"))

	def test_non_admin_cannot_add_university(self):
		self.client.post(self.login_url, {'username' : "normaluser", 'password' : "12345"})
		response = self.client.post(self.university_url, {'name' : "Better University", 'location' : "Better Place"})
		self.assertTemplateUsed(response, "WOF/error_page.html")


	def test_admin_add_course(self):
		writeUniversityToXML(self.university.slug)
		self.client.post(self.login_url, {'username' : "admin", 'password' : "12345"})
		response = self.client.post(self.course_url, {'university' : self.university.pk, 'name' : "Basic course", 
													'level' : 1, 'credits' : 10, 'courseConvener' : "TestUser",
													'courseNumber' : "TEST2012"})
		self.assertTrue(Course.objects.filter(courseNumber="TEST2012").exists())

	def test_non_admin_cannot_add_course(self):
		self.client.post(self.login_url, {'username' : "normaluser", 'password' : "12345"})
		response = self.client.post(self.course_url, {'university' : self.university.pk, 'name' : "Basic course", 
													'level' : 1, 'credits' : 10, 'courseConvener' : "TestUser",
													'courseNumber' : "TEST2012"})
		self.assertTemplateUsed(response, "WOF/error_page.html")

class TestDeleteViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.login_url = reverse("WOF:user_login")
		self.course_url = reverse("WOF:add_course")

		self.basic_admin_user = User.objects.create(username="admin")
		self.basic_admin_user.set_password("12345")
		self.basic_admin_user.save()

		self.admin_student = StudentUser.objects.create(user=self.basic_admin_user, isAdmin=True)
		self.admin_student.save()

		self.basic_non_admin_user = User.objects.create(username="normaluser")
		self.basic_non_admin_user.set_password("12345")
		self.basic_non_admin_user.save()

		self.basic_non_admin_student = StudentUser.objects.create(user=self.basic_non_admin_user, isAdmin=False)
		self.basic_non_admin_student.save()

		self.university = University.objects.create(name="Test University", location="Test Land")
		self.course = Course.objects.create(university=self.university, 
			name="Basic course", level=1, credits=10, courseConvener="TestUser", courseNumber="TEST2012")

	def test_admin_delete_course(self):
		self.client.post(self.login_url, {'username' : "admin", 'password' : "12345"})
		response = self.client.post(reverse("WOF:delete_course", args=(self.course.slug,)))

		self.assertFalse(Course.objects.filter(courseNumber="TEST2012").exists())
		
	def test_non_admin_cannot_delete_course(self):
		self.client.post(self.login_url, {'username' : "normaluser", 'password' : "12345"})
		response = self.client.post(reverse("WOF:delete_course", args=(self.course.slug,)))

		self.assertTrue(Course.objects.filter(courseNumber="TEST2012").exists())