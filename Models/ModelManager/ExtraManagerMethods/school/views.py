from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
	student = Student.students.get_stu_roll_range(2,5)
	return render(request,'school/home.html',{'student':student})
