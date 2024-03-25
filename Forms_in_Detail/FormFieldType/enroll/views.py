from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
# Create your views here.




def AddStudent(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		
		if form.is_valid():
			print(form.is_valid())
			name = form.cleaned_data['roll']
			print(form.cleaned_data['rate'])
		
			

	else:
		form = StudentForm()  
		print("this is get request")                     
	return render(request,'enroll/add.html',{'form':form})
