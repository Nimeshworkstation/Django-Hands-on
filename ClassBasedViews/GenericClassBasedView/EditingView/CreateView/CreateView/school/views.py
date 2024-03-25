from django.shortcuts import render
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.
class StudentCreateView(CreateView):
	model = Student
	#success_url = '/thanks/'
	fields = ['name','email','password']
	#By default it takes name student_form, we can replace it using this code
	template_name = 'school/sform.html'

class ThanksTemplateView(TemplateView):
	template_name = 'school/thanks.html'

class StudentDetailView(DetailView):
	model = Student


