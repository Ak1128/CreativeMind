from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import message, send_mail, BadHeaderError

# Create your views here.
from .models import *
from .forms import CreateUserForm , ContactForm

def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'books/register.html', context)


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'books/login.html', context)


@csrf_exempt
def logoutUser(request):
	logout(request)
	return redirect('base')

def base(request):
  return render(request,'books/base.html')

@login_required(login_url='login')
def home(request):
  return render(request,'books/index.html')


@login_required(login_url='login')
def dashboardPage(request):
	return render(request,'books/dashboard.html')



@login_required(login_url='login')
def schedulePage(request):
	return render(request,'books/schedule.html')


@login_required(login_url='login')
def bookPage(request):
	return render(request,'books/book.html')



@login_required(login_url='login')
def gatePage(request):
	return render(request,'books/gate.html')

@login_required(login_url='login')
def catPage(request):
	return render(request,'books/cat.html')

@login_required(login_url='login')
def netPage(request):
	return render(request,'books/net.html')

@login_required(login_url='login')
def jeemainPage(request):
	return render(request,'books/jeemain.html')









