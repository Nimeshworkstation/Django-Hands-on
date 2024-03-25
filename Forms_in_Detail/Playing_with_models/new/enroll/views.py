from django.shortcuts import render
from .models import Student
# Create your views here.


def ViewStudent(request):
	stud = Student.objects.get(id=2)
	return render(request,'enroll/home.html',{'stud':stud})
