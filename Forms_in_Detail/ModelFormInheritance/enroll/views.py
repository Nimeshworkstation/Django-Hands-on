from django.shortcuts import render
from .forms import StudentForm, TeacherForm
from .models import User


# Create your views here.
''' this is instance method to update'''

def student_form(request): 
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:  
        form = StudentForm()
    return render(request, 'enroll/student.html', {'form': form})


def teacher_form(request): 
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    else:  
        form = TeacherForm()
    return render(request, 'enroll/teacher.html', {'form': form})
