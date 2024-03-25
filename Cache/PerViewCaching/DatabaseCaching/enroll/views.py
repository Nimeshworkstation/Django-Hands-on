from django.shortcuts import render
from django.views.decorators.cache import cache_page

# first method of creating 
@cache_page(60)
def home(request):
	return render(request,'enroll/home.html')

#second method of creating caching from urls
#in case two urls hit same view function where one url uses cache and another dont uses cache
def contact(request):
	return render(request,'enroll/contact.html')
