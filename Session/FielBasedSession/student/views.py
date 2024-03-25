from django.shortcuts import render,HttpResponse



def setsession(request):
	request.session['name'] = 'Sonam'
	return render(request,'student/setsession.html')


def getsession(request):
	if 'name' in request.session:
		val = request.session['name']
		request.session.modified = True
		return render(request,'student/getsession.html',{'name':val})
	else:
		return HttpResponse("your session has expired !! ")
def delsession(request):
	request.session.flush()
	request.session.clear_expired() # this is used to clear all the database entry of sessions that are expired
	return render(request,'student/delsession.html')

