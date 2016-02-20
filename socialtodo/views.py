from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from itertools import chain

from socialtodo.forms import RegForm, LoginForm, TaskCreate, ValidationError
from socialtodo.models import Task


# Create your views here.
def errors_to_strings(argument):
    switcher = {
        'invalid_email': "Invalid email address",
        'name_too_short': "name too short",
        'name_too_long': "name too long",
        'email_too_short': "email too short",
        'email_too_long': "email too long",
        'pw_too_short': "password too short",
        'pw_too_long': "password too long",
        'user_exists': "Account with this email already exists!",
        'invalid_password': "Invalid password",
        'invalid_input' : "Please fill in all required fields",
        'passwords_match_fail' : "Passwords don't match"
    }
    return switcher.get(argument, argument)

def index(request):
	if request.method == 'GET':
		error = request.GET.get('error','')
		error = errors_to_strings(error)
	if not request.user.is_anonymous():
		l1 = Task.objects.filter(owner=request.user)
		l2 = Task.objects.filter(collab1=request.user.email)
		l3 = Task.objects.filter(collab2=request.user.email)
		l4 = Task.objects.filter(collab3=request.user.email)
		tasks = list(chain(l1,l2,l3,l4))

		return render(request, 'socialtodo/index.html', {
		'task_form': TaskCreate,
		'tasks': tasks,
		'error': error,
		})

	else: 
		return render(request, 'socialtodo/index.html', {
		'reg_form': RegForm, 
		'login_form': LoginForm, 
		'error': error
		})

def user_register(request):
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			try:
				data = form.cleaned_data
				_email = data['email']
				_pw = data['password']
				form.save()
				user = authenticate(username=_email, password=_pw) 
				login(request, user)
			except Exception as error:
				return HttpResponseRedirect('/?error='+str(error)[1:-1])
			return HttpResponseRedirect('/')
		return HttpResponseRedirect('/?error=invalid_input')
	return HttpResponse(403)

def user_login(request):
	if request.method == 'POST':
		errors = []
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			_email = data['email']
			_username = _email
			_pw = data['password']
			if len(User.objects.filter(email=_email)) == 0:
				return HttpResponseRedirect('/?error=invalid_email')
			user = authenticate(username=_username, password=_pw) 
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/?error=invalid_password')
	return HttpResponse('This is the login page')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def task_create(request):
	if request.method == 'POST':
		errors = []
		form = TaskCreate(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			_title = data['title']
			_desc = data['description']
			
			_collab1 = data['collaborator1']
			_collab2 = data['collaborator2']
			_collab3 = data['collaborator3']			
			task = Task.create(owner=request.user, title=_title)
			if len(_desc) != 0:
				task.description = _desc
			task.collab1 = _collab1
			task.collab2 = _collab2
			task.collab3 = _collab3
			task.save()
			return HttpResponseRedirect('/')
	return HttpResponse('This is the task creation page')

def task_complete(request):
	if request.method == 'POST':
		taskId = request.POST.get("taskId","")
		task = Task.objects.get(id = taskId)
		if task.isComplete:
			task.isComplete = False
			task.save()
		else:
			task.isComplete = True
			task.save()
		return HttpResponseRedirect('/')
	return HttpResponse('This is the task completion page')

def task_delete(request):
	if request.method == 'POST':
		taskId = request.POST.get("taskId","")
		Task.objects.get(id = taskId).delete()
		return HttpResponseRedirect('/')
	return HttpResponse('This is the task deletion page')
