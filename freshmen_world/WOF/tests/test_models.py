from django.test import TestCase
from WOF.models import *
import datetime as datetime

class TestUniversity(TestCase):

	def setUp(self):
		self.university1 = University.objects.create(
				name='Edinburgh University',
				location='Edinburgh',
			)

	def test_university_is_assigned_slug(self):
		self.assertEquals("edinburgh-university", self.university1.slug)

	def test_university_name_unique(self):
		self.assertEquals(self.university1, University.objects.get(name="Edinburgh University"))

class TestStudentUser(TestCase):

	def setUp(self):
		self.university = University.objects.create(
				name="Test University",
				location="Test",
			)

		self.user = User.objects.create(username="testname", password="passtests")
		self.student_user = StudentUser.objects.create(user=self.user,
														university=self.university,
														degree="passing tests",
														level=1,
														isAdmin=False,
														)
	def test_student_user_name(self):
		self.assertEquals("testname", str(self.student_user))

	def test_student_user_university(self):
		self.assertEquals(self.university, self.student_user.university)

	def test_student_user_unique(self):
		self.assertEquals(self.student_user, StudentUser.objects.get(user=self.user))


class TestTask(TestCase):

	def setUp(self):
		self.university1 = University.objects.create(
				name='Edinburgh University',
				location='Edinburgh',
			)

		self.user = User.objects.create(username="Sam", 
									password="testcase",)
		self.student_user = StudentUser.objects.create(user=self.user,
												university=self.university1,
												degree="graduate with food",
												level=3,
												isAdmin=False,
												)


		self.task1 = Task.objects.create(
				name="Pass the test",
				completed=False,
				dueDate=datetime.datetime(2022, 3, 28),
				timePlanned=datetime.time(18,30),
				studentUser=self.student_user,
			)

	def test_task_is_assigned_slug(self):
		self.assertEquals("pass-the-test", self.task1.slug)

	def test_task_student_user(self):
		self.assertEquals(self.student_user, self.task1.studentUser)

	def test_task_name_unique(self):
		self.assertEquals(self.task1, Task.objects.get(name="Pass the test"))

class TestCourses(TestCase):

	def setUp(self):
		self.university = University.objects.create(
				name="Test University",
				location="Test",
			)

		self.course = Course.objects.create(name="Passing Tests 101",
											level=2,
											credits=10,
											courseConvener="John Williamson",
											courseNumber="TEST2022",
											university=self.university,
											)

	def test_course_slug(self):
		self.assertEquals("passing-tests-101", self.course.slug)

	def test_course_number_unique(self):
		self.assertEquals(self.course, Course.objects.get(courseNumber="TEST2022"))
