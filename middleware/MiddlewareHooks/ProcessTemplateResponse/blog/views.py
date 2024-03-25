from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
	print("-------------------------------")
	print("---I am View---")
	print("-------------------------------")
	context = {'name': 'Nimesh'}
	
	return TemplateResponse(request,'blog/home.html',context)
