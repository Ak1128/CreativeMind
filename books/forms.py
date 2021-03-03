from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, get_connection



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


from django.forms.widgets import Textarea

# Create your models here.

class ContactForm(forms.Form):
	fname 	= forms.CharField(label='Full Name',max_length=100 , required= True)

	email		= forms.EmailField(label ='Email Address', max_length=100 , required=False)

	subject = forms.CharField(max_length=100)


	message = forms.CharField(label='Comment', widget=Textarea)

	def __str__(self):
		return self.fname

def contactPage(request):
     submitted = False
     if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             # assert False
             con = get_connection('django.core.mail.backends.console.EmailBackend')
             send_mail(
                 cd['subject'],
                 cd['message'],
                 cd.get('email', 'noreply@example.com'),
                 ['mypersonalworkcontrol@gmail.com'],
                 connection=con
             )
             return HttpResponseRedirect('/contact')
     else:
         form = ContactForm()
         if 'submitted' in request.GET:
             submitted = True
 
     return render(request, 'books/contact.html', {'form': form, 'submitted': submitted})