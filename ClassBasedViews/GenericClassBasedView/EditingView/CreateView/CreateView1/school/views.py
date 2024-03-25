from django.shortcuts import render
from .models import Student
from django import forms
from .forms import StudentForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.
#First method to add class and widget to our form
'''
class StudentCreateView(CreateView):
	model = Student
	success_url = '/thanks/'
	fields = ['name','email','password']

	#adding a field class to the form elements so that we can use css and bootstrap etc
	def get_form(self):
		form = super().get_form()
		form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
		form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'passclass'})
		return form

'''


# Second Method to add Class and widget to our Form, by using model form in forms.py
class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
	template_name = 'school/thanks.html'




