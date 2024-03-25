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
            rg = User(name=nm,email=em,password=pwd) #used for Insert
            #rg = User(id=1,name=nm,email=em,password=pwd) passing an id updates the data of id that is given, here data of id 1 is updated
            rg.save()
            #the below codes are used to delete item using id
            #reg=User(id=1)
            #reg.delete()

    else:
        form = StudentForm()
        print("this is get request")

    return render(request, 'enroll/add.html', {'form': form})
