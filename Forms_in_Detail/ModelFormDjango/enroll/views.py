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
            

    else:
        form = StudentForm()
        print("this is get request")

    return render(request, 'enroll/add.html', {'form': form})
