from django.shortcuts import render
from .models import Student, ProxyStudent
# Create your views here.

def home(request):
	#student = Student.objects.all()
	#student = ProxyStudent.students.get_stu_roll_range(2,5)
	student = ProxyStudent.students.all()
	return render(request,'school/home.html',{'student':student})
