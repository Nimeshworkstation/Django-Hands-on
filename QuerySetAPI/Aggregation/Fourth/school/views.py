from django.shortcuts import render
from .models import Student, Teacher
from datetime import date, time
import datetime 
from django.db.models import Avg, Sum, Min, Max, Count



# Create your views here.
def home(request):
	
	student = Student.objects.all()
	avg = student.aggregate(Avg('marks'))
	total = student.aggregate(Sum('marks'))
	minimun = student.aggregate(Min('marks'))
	maximun = student.aggregate(Max('marks'))
	totalcount = student.aggregate(Count('marks'))
	print(avg)
	
	print("Return:", student)
	print()
	print("SQL QUERY:",student.query)
	return render(request,'school/home.html',{'student':student,'avg':avg,'miny':minimun, 'maxy':maximun,'totct':totalcount,'tot':total})



