from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q



# Create your views here.
def home(request):
	#student = Student.objects.all()

	#student = Student.objects.filter(city="Essen")
	
	#student = Student.objects.exclude(city="Essen")
	
	#student = Student.objects.order_by('city')
	#student = Student.objects.order_by('?')
	#student = Student.objects.order_by('-marks')
	#student = Student.objects.order_by('marks')
	#student = Student.objects.order_by('name')
	
	#student = StudentAobjects.order_by('id').reverse()[:5]

	
	#student = Student.objects.values()

	#student = Student.objects.values('name','city')
	
	#student = Student.objects.values_list()
	#student = Student.objects.values_list('id','name', named = True)
	#student = Student.objects.values('id','name')

	#student = Student.objects.using('default')
	
	#student = Student.objects.dates('pass_date','month')
	#student = Student.objects.dates('pass_date','year')


	############Second Table's Teacher started ###########################
	
	#qs1 = Student.objects.values_list('id','name', named =True)
	#qs2 = Teacher.objects.values_list('id','name',named= True)
	#student = qs2.union(qs1)


	#qs1 = Student.objects.values_list('id','name', named =True)
	#qs2 = Teacher.objects.values_list('id','name',named= True)
	#student = qs2.union(qs1, all = True)


	#qs1 = Student.objects.values_list('id','name', named =True)
	#qs2 = Teacher.objects.values_list('id','name',named= True)
	#student = qs2.intersection(qs1)


	#qs1 = Student.objects.values_list('id','name', named =True)
	#qs2 = Teacher.objects.values_list('id','name',named= True)
	#student = qs1.difference(qs2)# It means qs1-qs2


#################### AND OR Operator ##############
	
	#student = Student.objects.filter(id=8) & Student.objects.filter(roll=12)
	#student = Student.objects.filter(id=8,roll=12)
	#student = Student.objects.filter(     Q(id=8) & Q(roll=12))
	
	#student = Student.objects.filter(id=3) | Student.objects.filter(roll=12)
	student = Student.objects.filter(     Q(id=3) | Q(roll=12))
	
	print("Return:", student)
	print("SQL QUERY:",student.query)
	return render(request,'school/home.html',{'student':student})



