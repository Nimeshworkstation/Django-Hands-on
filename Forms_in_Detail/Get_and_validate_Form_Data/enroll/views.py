from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def AddStudent(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		
		if form.is_valid():
			print(form.is_valid())
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			print(name,email,password)
	else:
		form = StudentForm()  
		print("this is get request")                     
	return render(request,'enroll/add.html',{'form':form})
