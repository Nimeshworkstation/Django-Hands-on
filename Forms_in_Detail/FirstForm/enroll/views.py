from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def AddStudent(request):
	form = StudentForm(auto_id=True, label_suffix='',initial={'uname':'Nimesh'})                             
	return render(request,'enroll/add.html',{'form':form})
