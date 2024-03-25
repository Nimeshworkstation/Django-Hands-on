from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def AddStudent(request):
	form = StudentForm()                       
	return render(request,'enroll/add.html',{'form':form})
