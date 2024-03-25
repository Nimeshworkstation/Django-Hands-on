from django.shortcuts import render



def setsession(request):
	request.session['name'] = 'Sonam'
	request.session['lname'] = 'Jha'
	return render(request,'student/setsession.html')


def getsession(request):
	#val = request.session['name']
	val = request.session.get('name', default = 'Guest')
	lname = request.session.get('lname', default = 'Guest')
	return render(request,'student/getsession.html',{'name':val,'lname':lname})

def delsession(request):
	del request.session['name']
	del request.session['lname']
	return render(request,'student/delsession.html')

