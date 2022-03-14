from django import forms
from WOF.models import StudentUserProfile
from django.contrib.auth.models import User

class StudentUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password',)

class StudentUserProfileForm(forms.ModelForm):
	class Meta:
		model = StudentUserProfile
		fields = ('email', 'university', 'degree', 'level', )