from django import forms
from WOF.models import *
from django.contrib.auth.models import User


class StudentUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email')

		widgets = {
			'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
			'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'}),
			'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
		}

		help_texts = {
			'username' : None,
			'password' : None,
			'email' : None,
		}

		labels = {
			'username' : "",
			'password' : "",
			'email' : "",
		}

	def __init__(self, *args, **kwargs):
		super(StudentUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = False

class StudentUserProfileForm(forms.ModelForm):
	class Meta:
		model = StudentUser
		fields = ('university', 'degree', 'level', 'isAdmin')

		widgets = {
			'degree' : forms.TextInput(attrs={'placeholder' : 'Degree name', }),
			'level' : forms.NumberInput(attrs={'placeholder' : "University Year", 'min':1, 'max':10}),
			'isAdmin': forms.CheckboxInput(attrs={})
		}
	
		labels = {
			'university' : "",
			'degree' : "",
			'level' : "",
			'isAdmin': "Admin",
		}


	def __init__(self, *args, **kwargs):
		super(StudentUserProfileForm, self).__init__(*args, **kwargs)
		self.fields['university'].required = False
		self.fields['degree'].required = False
		self.fields['level'].required = False

class StudentUserChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password', 'email',)

		widgets = {
			'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
			'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'}),
			'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
			'first_name' : forms.TextInput(attrs={'placeholder' : 'First name'}),
			'last_name' : forms.TextInput(attrs={'placeholder' : 'Last name'}),
		}

		help_texts = {
			'username' : None,
			'password' : None,
			'email' : None,
		}

		labels = {
			'username' : "",
			'password' : "",
			'email' : "",
			'first_name': "",
			'last_name': "",
		}

	def __init__(self, *args, **kwargs):
		super(StudentUserChangeForm, self).__init__(*args, **kwargs)
		# self.fields['email'].required = False
		self.fields['first_name'].required = False
		self.fields['last_name'].required = False

class StudentUserChangeProfileForm(forms.ModelForm):
	class Meta:
		model = StudentUser
		fields = ('university', 'degree', 'level', 'isAdmin')

		widgets = {
			'degree' : forms.TextInput(attrs={'placeholder' : 'Degree name', }),
			'level' : forms.NumberInput(attrs={'placeholder' : "University Year", 'value':"", 'min': '1','max':10}),
			'isAdmin': forms.CheckboxInput(attrs={}),
		}
	
		labels = {
			'university' : "",
			'degree' : "",
			'level' : "",
			'isAdmin': "Admin",
		}


	def __init__(self, *args, **kwargs):
		super(StudentUserChangeProfileForm, self).__init__(*args, **kwargs)
		self.fields['university'].required = False
		self.fields['degree'].required = False
		self.fields['level'].required = False

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = (
			'name', 'level', 'credits', 'courseConvener', 
			'courseNumber', 'university',
			)

		labels = {
			'name': "",
			'level': "",
			'credits': "",
			'courseConvener': "",
			'courseNumber': "",
			'university': "",
		}

		widgets = {
			'name':  forms.TextInput(attrs={'placeholder' : 'Course name'}),
			'level': forms.NumberInput(attrs={'placeholder' : 'Course Level'}),
			'credits': forms.NumberInput(attrs={'placeholder' : 'Credits'}),
			'courseConvener' : forms.TextInput(attrs={'placeholder' : 'Course Head'}),
			'courseNumber' : forms.TextInput(attrs={'placeholder' : 'Course Number'}),
		}

class UniversityForm(forms.ModelForm):
	class Meta:
		model = University
		fields = (
			'name',
			'location',
			)

		labels = {
			'name' : "",
			'location' : "",
		}

		widgets = {
			'name' : forms.TextInput(attrs={'placeholder' : "University Name"}),
			'location' : forms.TextInput(attrs={'placeholder' : "Location"}),
		}