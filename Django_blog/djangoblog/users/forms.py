from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=64, label='First Name')
	last_name = forms.CharField(max_length=64, label='Last Name')
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	first_name = forms.CharField(max_length=64, label='First Name', required=False)
	last_name = forms.CharField(max_length=64, label='Last Name', required=False)
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

