from django.shortcuts import render
from .forms import SignupForm 
from django.contrib import messages  
# Create your views here.

def signup(request):
	if request.method == "POST":
		fm = SignupForm(request.POST)
		if fm.is_valid():
			messages.success(request, 'Account created successfully !!' )
			fm.save()

	else:
		fm = SignupForm()
	return render (request,'enroll/signup.html',{'fm': fm})




