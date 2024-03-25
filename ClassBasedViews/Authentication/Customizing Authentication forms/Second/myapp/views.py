from django.shortcuts import render
from .forms import LoginForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView, PasswordChangeDoneView

# Create your views here.

class MyDashboardView(TemplateView):
	template_name = 'myapp/dashboard.html'

	
class MyLoginView(LoginView):
	template_name = 'myapp/login.html'
	authentication_form = LoginForm

class MyLogoutView(LogoutView):
	template_name = 'myapp/logout.html'

class MyPasswordChangeView(PasswordChangeView):
	template_name = 'myapp/changepass.html'
	success_url = '/changepassdone/'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = 'myapp/changepassdone.html'


