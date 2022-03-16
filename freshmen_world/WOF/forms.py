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
		fields = ('university', 'degree', 'level', )

		widgets = {
			'university' : forms.TextInput(attrs={'placeholder' : 'University', }),
			'degree' : forms.TextInput(attrs={'placeholder' : 'Degree name', }),
			'level' : forms.NumberInput(attrs={})
		}
	
		labels = {
			'university' : "",
			'degree' : "",
			'level' : "",
		}


	def __init__(self, *args, **kwargs):
		super(StudentUserProfileForm, self).__init__(*args, **kwargs)
		self.fields['university'].required = False
		self.fields['degree'].required = False
		self.fields['level'].required = False