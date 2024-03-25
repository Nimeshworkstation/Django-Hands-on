from django.shortcuts import render

# Create your views here.
def feesInfo(request):
	return render(request,'fees/info.html',{'nm':'dango_fees'})