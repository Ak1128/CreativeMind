from django.contrib import admin
from django.urls import path,include
from . import views
from .import forms
from django.contrib.auth import views as auth_views


# Urls 
urlpatterns = [
    path('',views.base, name="base"),
		path('home/',views.home, name="home"),
    path('dashboard/',			views.dashboardPage   , name='dashboard'),
		path('examshedules/',		views.schedulePage 		,	name='schedule'),
		
		path('book/',		views.bookPage 		,	name='book'),
		path('contact/',				forms.contactPage 		,	name='contact'),
		path('cat/',						views.catPage 				,	name='cat'),
		path('net/',						views.netPage 				,	name='net'),
		path('gate/',						views.gatePage 				,	name='gate'),
		path('jeemain/',				views.jeemainPage 		,	name='jeemain'),
		path('register/', 			views.registerPage		, name="register"),
		path('login/', 					views.loginPage				, name="login"),  
		path('logout/', 				views.logoutUser			, name="logout"),
		path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="books/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="books/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="books/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="books/password_reset_done.html"), 
        name="password_reset_complete"),


]