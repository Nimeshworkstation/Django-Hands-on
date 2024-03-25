from django.shortcuts import render
from .models import ExamCenter, MyExamCenter
# Create your views here.

def home(request):
	exam = ExamCenter.objects.all()
	mexam = MyExamCenter.objects.all()

	return render(request,'school/home.html',{'exam':exam,'mexam':mexam})
