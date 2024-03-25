from django.shortcuts import render
from .models import Student, Teacher, Contractor
# Create your views here.

def home(request):
	student = Student.objects.all()
	contractor = Contractor.objects.all()
	teacher = Teacher.objects.all()
	

	return render(request,'school/home.html',{'student':student,'teacher':teacher,'contractor':contractor})

