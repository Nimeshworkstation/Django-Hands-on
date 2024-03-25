from django.shortcuts import render

# Create your views here.
def show_details(request,roll):

	if roll==1:
		student = {'id':roll, 'name':'Nimesh'}
	if roll==2:
		student = {'id':roll, 'name':'Nimesh2'}

	if roll==3:
		student = {'id':roll, 'name':'Nimesh3'}
	return render(request,'enroll/show.html',student)

def show_subdetails(request,roll,sub):

	if roll==1 and sub ==4:
		student = {'id':roll, 'name':'Nimesh','subject':'subject 4'}
	if roll==2 and sub ==5:
		student = {'id':roll, 'name':'Nimesh2','subject':'subject 5'}

	if roll==3 and sub==6:
		student = {'id':roll, 'name':'Nimesh3','subject':'subject 6'}
	return render(request,'enroll/show.html',student)


def home(request):
	return render(request,'enroll/home.html')