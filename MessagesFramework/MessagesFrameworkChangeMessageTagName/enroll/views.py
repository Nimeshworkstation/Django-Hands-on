from django.shortcuts import render
from .forms import StudentReg
from django.contrib import messages

# Create your views here.
def regi(request):
	if request.method == "POST":
		fm = StudentReg(request.POST)
		if fm.is_valid():
			fm.save()
			#First method of sending messages
			messages.add_message(request,messages.INFO,"Now you can login this is my check to write info ant bla bla bal bla bla bla blab  !!!")
			messages.add_message(request,messages.SUCCESS,"YOUR ACCOUNT IS CREATED")
			#second Method of sending messages
			messages.error(request,"it is a error meesage")
			
			messages.warning(request,"it is a warning message")

	else:
		fm=StudentReg()
	return render(request,'enroll/userregistration.html',{'form':fm})