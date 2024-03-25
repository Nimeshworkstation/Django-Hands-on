from django.shortcuts import render

# Create your views here.
def setcookie(request):
	response = render(request,'student/setcookie.html')
	response.set_cookie('name','sonam')
	return response


def getcookie(request):
	#name = request.COOKIES['name']
	name = request.COOKIES.get('name',"Guest")
	return render(request,'student/getcookie.html',{'name':name})


def delcookie(request):
	response = render(request,'student/deletecookie.html')
	response.delete_cookie('name')
	return response