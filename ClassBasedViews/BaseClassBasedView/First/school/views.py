from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

#Function Based View
def myview(request):
	return HttpResponse('<h1> this is function based view </h1>')

#Class Based View
class MyView(View):
	name = "Nimesh"
	def get(self, request):
		#return HttpResponse('<h1> this is class based view </h1>')
		#return HttpResponse(self.name)
		return HttpResponse(self.name)



class MyViewChild(MyView):
	def get(self,request):
		return HttpResponse(self.name)