from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
	print("-------------------------------")
	print("---I am View---")
	
	print("-------------------------------")
	a = 10/0
	return HttpResponse("This is Excp Page")
