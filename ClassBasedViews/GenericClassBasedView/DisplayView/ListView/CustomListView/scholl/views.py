from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView


# Create your views here.

class StudentListView(ListView):
	model = Student
	#this changes the default template name method scholl_list to scholl_get
	template_name_suffix = '_get'