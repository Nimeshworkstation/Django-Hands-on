from django.shortcuts import render
from .models import Student, ExamCenter

# Create your views here.
def home(request):
	student = Student.objects.all()
	Exam = ExamCenter.objects.all()
	return render(request,'school/home.html',{'student':student,'teacher':Exam,})

