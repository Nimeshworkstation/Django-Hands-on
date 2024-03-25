from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
from django.template import loader 
from django.http import HttpResponse
from .forms import empforms
from django.contrib import messages
# Create your views here.

def main(request):
	return render(request,'web/main.html')



def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        context = {'msg': 'Success'}
        return render(request,'web/index.html', context )
    else:

        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)


def detail(request):
	detail_list = Member.objects.all()
	context = { 'detail_list': detail_list, }
	return render(request,'web/detail.html', context)

def edit(request, id):
	displayemp = Member.objects.get(id=id)
	return render(request,'web/edit.html',{"Member":displayemp})


def update(request,id):
	updateemp = Member.objects.get(id=id)
	form = empforms(request.POST, instance=updateemp)
	#if form.is_valid():
	form.save()
	messages.success(request,"Record updated succesfully")
	return render(request,'web/edit.html',{"Member":updateemp})
		#else:
		#	return render(request,'web/detail.html')
