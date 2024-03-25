
from .models import Student
from .forms import StudentForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


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

class StudentDeleteView(DeleteView):
	model = Student
	success_url = '/create/'
	template_name = 'school/studentdelete.html'


