from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
#Function View
def homefunc(request):
	return render(request,'school/home.html')


#Class Based View
class HomeClassView(View):
	def get(self,request):
		return render(request,'school/home.html')


#############################################################
                     #Using Context#



def aboutfunc(request):
	context = {'msg': 'Welcome to Nimesh Function Based Views'}
	print(context)
	return render(request,'school/about.html',context)



class AboutClassView(View):
	def get(self,request):
		context = {'msg':'Welcome to Nimesh Class based views'}
		return render(request,'school/about.html',context)

#################################################
                  #Using Post Method#

def contactfunc(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name'])
			return HttpResponse('Thank you Form submitted !')
	else:
		form = ContactForm()
		return render(request,'school/contact.html',{'form':form})




class ContactClassView(View):
	def get(self, request):
		form = ContactForm()
		return render(request,'school/contact.html',{'form':form})

	def post(self,request):
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name'])
			return HttpResponse('Thank you Form submitted !')



###################################################################

'''  One Example of using template_name in function based views 
######################################
def newsfunc(request):
	template_name = 'school/news.html'
	context = {'info':'CIB enquiry Why nimesh is poor ? '}
	return render(request,template_name,context)
######################################## ''' 


#This  function base method is used by two url to render two different html files
def newsfunc(request,template_name):
	template_name = template_name
	context = {'info':'CIB enquiry Why nimesh is poor ? '}
	return render(request,template_name,context)


#This is simple Example of using template_name in class based views
'''
class NewsClassView(View):
	template_name = 'school/news1.html'
	def get(self,request):
		context = {'info':'CIB inquiry where is nimesh'}
		return render(request,self.template_name,context)

'''

#This class is used by two urls to render two different html files
class NewsClassView(View):
	template_name = ''
	def get(self,request):
		context = {'info':'CIB inquiry where is nimesh'}
		return render(request,self.template_name,context)

