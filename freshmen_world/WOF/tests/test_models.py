from django.test import TestCase
from WOF.models import *
import datetime as datetime

class TestUser(TestCase):
	

class TestUniversity(TestCase):

	def setUp(self):
		self.university1 = University.objects.create(
				name='Edinburgh University',
				location='Edinburgh',
			)

	def test_university_is_assigned_slug(self):
		self.assertEquals(self.university1.slug, "edinburgh-university")

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
		self.assertEquals(self.task1.slug, "pass-the-test")