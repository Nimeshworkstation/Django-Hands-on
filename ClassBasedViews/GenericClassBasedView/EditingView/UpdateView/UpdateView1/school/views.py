from django.shortcuts import render
from .models import Student
from django import forms
from .forms import StudentForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
#First method to set class in update forms
'''
class StudentCreateView(CreateView):
	model = Student
	fields = ['name','email','password']
	success_url = '/thanks/'

	def get_form(self):
		form = super().get_form()
		form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
		form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'passclass'})
		return form

class StudentUpdateView(UpdateView):
	model = Student
	fields = ['name','email','password']
	success_url = '/thanks/'

	def get_form(self):
		form = super().get_form()
		form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
		form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'passclass'})
		return form'''

class ThanksTemplateView(TemplateView):
	template_name = 'school/thanks.html'


class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = '/thanks/'

class StudentUpdateView(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = '/thanks/'


