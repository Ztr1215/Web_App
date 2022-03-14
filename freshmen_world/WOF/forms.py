from django import forms
from WOF.models import *
from django.contrib.auth.models import User

university_choices = ((str(counter+1), list(University.objects.all())[counter]) 
					for counter in range(len(University.objects.all())))

class StudentUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	# university = forms.ChoiceField(choices=['john', 'sam'])
	university = forms.ChoiceField(choices=university_choices)
	class Meta:
		model = User
		fields = ('username', 'password', 'university',)


class StudentUserProfileForm(forms.ModelForm):
	class Meta:
		model = StudentUserProfile
		fields = ('email', 'university', 'degree', 'level', )