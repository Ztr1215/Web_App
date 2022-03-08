from django import forms
from WOF.models import StudentUserProfile

class StudentUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password',)

class StudentUserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('email', 'university', 'degree', 'level', )