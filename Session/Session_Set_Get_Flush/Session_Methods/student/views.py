from django.shortcuts import render



def setsession(request):
	request.session['name'] = 'Sonam'
	request.session['lname'] = 'Jha'
	return render(request,'student/setsession.html')


def getsession(request):
	#val = request.session['name']
	val = request.session.get('name', default = 'Guest')
	lname = request.session.get('lname', default = 'Guest')
	keys = request.session.keys()
	items = request.session.items()
	#age= request.session.setdefault('age','26')

	return render(request,'student/getsession.html',{'name':val,'lname':lname,'keys':keys,'items':items})

def delsession(request):
	request.session.flush()
	return render(request,'student/delsession.html')

