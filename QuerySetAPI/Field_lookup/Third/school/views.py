from django.shortcuts import render
from .models import Student, Teacher
from datetime import date, time
import datetime 



# Create your views here.
def home(request):
	
	#student = Student.objects.all()
	#student = Student.objects.filter(name__exact='Nimesh') 
	#student = Student.objects.filter(name__iexact='Nimesh') 
	#student = Student.objects.filter(name__contains='a') 
	#student = Student.objects.filter(name__icontains='a') 
	#student = Student.objects.filter(id__in=[1,5,7]) 
	#student = Student.objects.filter(marks__in = [80,90]) 
	#student = Student.objects.filter(marks__gt = 60) 
	#student = Student.objects.filter(marks__gte = 45) 
	#student = Student.objects.filter(marks__lt = 80) 
	#student = Student.objects.filter(marks__lte = 80) 
	#student = Student.objects.filter(name__startswith = 'n') 
	#student = Student.objects.filter(name__istartswith = 'n') 
	#student = Student.objects.filter(name__endswith = 't') 
	#student = Student.objects.filter(name__iendswith = 't') 
	#student = Student.objects.filter(pass_date__range = ('2022-04-05','2022-04-14')) 
	#student = Student.objects.filter(admdatetime__date = datetime.date(2022,4,14)) 
	#student = Student.objects.filter(admdatetime__date__gt = datetime.date(2021,4,14)) 
	#student = Student.objects.filter(admdatetime__year = (2021)) 
	#student = Student.objects.filter(admdatetime__year__gt = (2021)) 
	#student = Student.objects.filter(admdatetime__year__gte = (2021)) 
	#student = Student.objects.filter(admdatetime__month = 4) 
	#student = Student.objects.filter(admdatetime__month__gt = 4) 
	#student = Student.objects.filter(admdatetime__month__gte = 4) 
	#student = Student.objects.filter(admdatetime__day = 7) 
	#student = Student.objects.filter(admdatetime__day__gt = 7) 
	#student = Student.objects.filter(admdatetime__day__gte = 7) 
	#student = Student.objects.filter(admdatetime__week = 15) 
	#student = Student.objects.filter(admdatetime__week__gt = 4) 
	#student = Student.objects.filter(admdatetime__week__gte = 4) 
	#student = Student.objects.filter(admdatetime__week_day = 5) 
	#student = Student.objects.filter(admdatetime__week_day__gt = 4) 
	#student = Student.objects.filter(admdatetime__quarter = 2) 
	#student = Student.objects.filter(admdatetime__time__gt =datetime.time(5,0)) 
	student = Student.objects.filter(admdatetime__hour = 7) 




	print("Return:", student)
	print()
	print("SQL QUERY:",student.query)
	return render(request,'school/home.html',{'student':student})



