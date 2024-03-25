from django.shortcuts import render



def setsession(request):
	request.session['name'] = 'Sonam'
	request.session.set_expiry(20) # with this code, session expires after 10 seconds 
	return render(request,'student/setsession.html')


def getsession(request):
	val = request.session['name']
	return render(request,'student/getsession.html',{'name':val})

def delsession(request):
	request.session.flush()
	request.session.clear_expired() # this is used to clear all the database entry of sessions that are expired
	return render(request,'student/delsession.html')

