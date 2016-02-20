from django import forms

from socialtodo.models import UserProfile, Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class ValidationError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class RegForm(forms.Form):
	fl_name = forms.CharField(label='your name', max_length=50)
	email = forms.EmailField(label='email address')
	password = forms.CharField(label='password', widget=forms.PasswordInput())
	password_confirmation = forms.CharField(label='confirm password', widget=forms.PasswordInput())

	class Meta:
		model = User

	def save(self):
		data = self.cleaned_data

		_name = data['fl_name']
		if len(_name) < 1:
			raise ValidationError('name_too_short')
		elif len(_name) > 30:
			raise ValidationError('name_too_long')

		_email = data['email']
		if len(_email) < 1:
			raise ValidationError('email_too_short')
		elif len(_email) > 30:
			raise ValidationError('email_too_long')
		elif User.objects.filter(email = _email):
			raise ValidationError('user_exists')
		_firstname = _name.split(" ")[0]
		_username = _email
		_pw = data['password']
		if len(_pw) < 1:
			raise ValidationError('pw_too_short')
		elif len(_pw) > 30:
			raise ValidationError('pw_too_long')
		_pw2 = data['password_confirmation']
		if _pw != _pw2:
			raise ValidationError('passwords_match_fail')
		user = User.objects.create_user(username=_username, email=_email, password=_pw, first_name=_firstname)
		user.save()

class LoginForm(forms.Form):
	email = forms.EmailField(label='email', max_length=50)
	password = forms.CharField(label='password', widget=forms.PasswordInput())

	class Meta:
		model = User	

class TaskCreate(forms.Form):
	title = forms.CharField(label='title', max_length=200)
	description = forms.CharField(label='description', max_length=500, required=False)
	collaborator1 = forms.EmailField(label='collaborator', required=False)
	collaborator2 = forms.EmailField(label='collaborator', required=False)
	collaborator3 = forms.EmailField(label='collaborator', required=False)

	class Meta:
		model = Task

