from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



class StudentDetailView(DetailView):
	model = Student
	#By defualt template name should be always student_detail.html
	#changing default template name from student_detail.html to our own template name, ie, here we have set our template name as student.html
	template_name = 'scholl/student.html'
	#changing default context name from student to stu
	#context_object_name = 'stu'
	#changing the name of pk in url student/<int:pk>/ to our own name here, for ex id
	#pk_url_kwarg = 'id'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['all'] = self.model.objects.all()
		return context 

class StudentListView(ListView):
	model = Student

	