from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import User


# Create your views here.
''' this is instance method to update'''

def AddStudent(request):
    if request.method == "POST":
        pi = User.objects.get(pk=1)
        form = StudentForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
        print("this is get request")

    return render(request, 'enroll/add.html', {'form': form})
