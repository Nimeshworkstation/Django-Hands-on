from django.shortcuts import render
from .models import Student
from django.db.models import Q


# Create your views here.
def home(request):

	student = Student.objects.all()[:5]
	print("Return:", student)
	print()
	print("SQL QUERY:",student.query)
	return render(request,'school/home.html',{'student':student})



