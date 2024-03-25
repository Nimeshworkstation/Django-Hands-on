from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import User


# Create your views here.


def AddStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            em=form.cleaned_data['email']
            nm=form.cleaned_data['name']
            pwd=form.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
            ''' this is one method to edit data with id=1'''
            #reg = User(id=1,name=nm,email=em,password=pwd)
            #reg.save()
            ''' this is method to delete data with id =1'''
            #reg=User(id=1)
            #reg.delete()
            

    else:
        form = StudentForm()
        print("this is get request")

    return render(request, 'enroll/add.html', {'form': form})
