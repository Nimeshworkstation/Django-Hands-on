from django.shortcuts import render

def courseInfo(request):
    return render(request,'course/info.html',{'nm':'dango_course'})