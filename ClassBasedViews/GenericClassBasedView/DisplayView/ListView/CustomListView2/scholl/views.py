from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView


# Create your views here.

class StudentListView(ListView):
	model = Student
	#this changes the default template name method scholl_list to student.html
	#but student_list can still be used , to do it
	#here we have changed the default template_name to student.html but if we remove 
	#student.html file from templates, django searches for default html and if it exists, it is rendered.
	template_name = 'scholl/student.html'
	#this changes the default context name student_list to students that is used in templates
	context_object_name = 'students'