from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
	print("-------------------------------")
	print("---I am View---")
	
	print("-------------------------------")
	
	return HttpResponse("This is Home Page")
