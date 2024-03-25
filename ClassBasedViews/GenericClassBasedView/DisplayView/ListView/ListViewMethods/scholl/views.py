from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView



#code to set cookie in a key named user and value nimesh
def setcookie(request):
	response = render(request,'scholl/setcookie.html')
	response.set_cookie('user','nimeshs')
	return response
# Create your views here.

class StudentListView(ListView):
	model = Student
	#this changes the default template name method scholl_list to student.html
	#but student_list can still be used , to do it
	#here we have changed the default template_name to student.html but if we remove 
	#student.html file from templates, django searches for default html and if it exists, it is rendered.
	template_name = 'scholl/student1.html'
	#this changes the default context name student_list to students that is used in templates
	context_object_name = 'students'

	#Using filter in queryset
	def get_queryset(self):
		return Student.objects.filter(course ='java')

	#Renaming context 
	def get_context_data(self, *args, **kwargs):
		print(args)
		print(kwargs)
		context = super().get_context_data(*args, **kwargs)
		context['fresher'] = Student.objects.all().order_by('name')
		return context

	def get_template_names(self):
		if self.request.COOKIES['user'] == 'nimesh':
			template_name = 'scholl/nimesh.html'
		else:
			template_name = self.template_name
		return [template_name]

