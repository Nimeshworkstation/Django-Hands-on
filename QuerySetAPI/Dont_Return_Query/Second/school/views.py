from django.shortcuts import render
from .models import Student, Teacher




# Create your views here.
def home(request):
	#student=Student.objects.get(name='Niket')
	
	#student=Student.objects.first()
	#student = Student.objects.order_by('name').first()
	#student = Student.objects.order_by('name').last()
	#student = Student.objects.latest('pass_date')
	#student = Student.objects.earliest('pass_date')

	
	#student = Student.objects.all()
	#print(student.exists())

	#one_data = Student.objects.get(pk=1)
	#print(student.filter(pk=one_data.pk).exists())
	#print(one_data)
	#student = Student.objects.create(name = 'Nitesh', roll = 78, city = 'Kirtipur', marks = 77, pass_date='2020-01-01')
	
	#student,created = Student.objects.get_or_create(name = 'Anisha', roll = 779, city = 'Kirtipur', marks = 77, pass_date='2020-01-01')
	#print(created)
	
	#student = Student.objects.filter(id=12).update(name='nikesh', marks=98)
	#student = Student.objects.filter(id=12).update(name='nikesh', marks=98)
	
	#student,created = Student.objects.update_or_create(id =14,name='Milan',defaults={'name': 'Nabin','roll':46,'marks':70,'pass_date':'2020-02-02'})
	#print(created)

	#student,created = Student.objects.update_or_create(id =14, name = 'Nabin',defaults={'city':'Nawalpur'})
	#print(created)

	#objs = [

		#Student(name='Atif',roll=112,city='Dortmund',marks=99, pass_date='2020-02-10'),
		#Student(name='Sonu',roll=113,city='Dortmund',marks=99, pass_date='2020-02-10'),
		#Student(name='Udit',roll=114,city='Dortmund',marks=99, pass_date='2020-02-10')


	#]

	#student = Student.objects.bulk_create(objs)
	
	#all_data = Student.objects.all()
	#for stu in all_data:
	#	stu.city = 'Kathmandu'
	#student = Student.objects.bulk_update(all_data,['city'])

	#student = Student.objects.in_bulk([1,2,3])
	#print(student[2].name)
	#student = Student.objects.in_bulk()
	#student = Student.objects.in_bulk([])

	#student = Student.objects.get(pk=14).delete()
	#student = Student.objects.filter(marks = 99).delete()
	#student = Student.objects.all.delete()


	#student = Student.objects.all()
	#print(student.count())


	print("Return:", student)
	
	return render(request,'school/home.html',{'student':student})



