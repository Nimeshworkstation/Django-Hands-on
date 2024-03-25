from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
# Create your views here.



def thankyou(request):
	return render(request,'enroll/succes.html')

def AddStudent(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		
		if form.is_valid():
			print(form.is_valid())
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			print(name,email,password)
			return HttpResponseRedirect('/enroll/success/')
			#return render(request,'enroll/succes.html',{'name': name})


	else:
		form = StudentForm()  
		print("this is get request")                     
	return render(request,'enroll/add.html',{'form':form})
