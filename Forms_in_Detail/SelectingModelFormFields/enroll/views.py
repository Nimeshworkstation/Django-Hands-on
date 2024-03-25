from django.shortcuts import render
from .forms import StudentForm
from .models import User


# Create your views here.
''' this is instance method to update'''

def showFormData(request):    
    form = StudentForm()
    return render(request, 'enroll/add.html', {'form': form})
