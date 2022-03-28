from django.test import TestCase, SimpleTestCase
from WOF.forms import *
from WOF.models import *


class TestStudentUserForm(TestCase):

	def test_student_form_valid_data(self):
		student_form = StudentUserForm(data={
				'username' : "testaccount",
				'password' : "test1",
		})

		self.assertTrue(student_form.is_valid())

	def test_student_form_invalid_data(self):
		student_form = StudentUserForm(data={
				'username' : "test account",
				'password' : "password123",
		})

		self.assertFalse(student_form.is_valid())

	def test_student_form_invalid_no_password(self):
		student_form = StudentUserForm(data={
				'username' : "test account",
				'password' : "",
		})

		self.assertFalse(student_form.is_valid())

class TestStudentUserProfileForm(TestCase):

	def setUp(self):
		self.test_uni = University.objects.create(name="Test University", 
									location="Test location")


	def test_student_profile_form_valid_data(self):
		student_profile_form = StudentUserProfileForm(data={
			'university' : self.test_uni.pk,
			'degree' : "How to Test",
			'isAdmin' : False,
			'level': 2
		})

		self.assertTrue(student_profile_form.is_valid())


	def test_student_profile_form_no_uni(self):
		student_profile_form = StudentUserProfileForm(data={
				'degree' : "How to test",
				'isAdmin' : False,
				'level' : 2,
		})

		self.assertTrue(student_profile_form.is_valid())

	def test_student_profile_admin_form(self):
		student_profile_form = StudentUserProfileForm(data={
				'isAdmin' : True,
		})

		self.assertTrue(student_profile_form.is_valid())

class TestCourseForm(TestCase):

	def setUp(self):
		self.test_uni = University.objects.create(name="Test University", 
									location="Test location")

	def test_course_form_valid(self):
		course_form = CourseForm(data={
			'name' : "Test Course",
			'level' : 2,
			'credits' : 10,
			'courseConvener' : "Test user",
			'courseNumber' : "TEST2001",
			'university' : self.test_uni.pk
		})

		self.assertTrue(course_form.is_valid())

	def test_course_form_invalid(self):
		course_form = CourseForm(data={
			'name' : "Test course",
			'level' : None,
			'credits' : 10,
			'courseConvener' : "Test user",
			'courseNumber' : "TEST2001",
			'university' : self.test_uni.pk
		})

		self.assertFalse(course_form.is_valid())

	def test_course_form_no_uni(self):
		course_form = CourseForm(data={
			'name' : "Test course",
			'level' : 2,
			'credits' : 10,
			'courseConvener' : "Test user",
			'courseNumber' : "TEST2001",
			'university' : None
		})

		self.assertFalse(course_form.is_valid())

class TestUniversityForm(TestCase):

	def test_university_form_valid_data(self):
		university_form = UniversityForm(data={
			'name' : "Glasgow University",
			'location' : "Glasgow",
		})

		self.assertTrue(university_form.is_valid())

	def test_university_form_no_name(self):
		university_form = UniversityForm(data={
			'name' : None,
			'location' : "Glasgow",
		})

		self.assertFalse(university_form.is_valid())

	def test_university_form_no_location(self):
		university_form = UniversityForm(data={
			'name': "Glasgow University",
			'location' : None,
		})

		self.assertFalse(university_form.is_valid())