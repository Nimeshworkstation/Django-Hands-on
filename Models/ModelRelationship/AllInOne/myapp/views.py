from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Page, Song

# Create your views here.


def show_song(request):
	data1 = Song.objects.all()
	print(data1[4])
	data2 = Song.objects.filter(song_duration = '7')
	data3 = Song.objects.filter(user__first_name = 'Madhu')

	return render(request,'myapp/song.html',{'data1':data1,'data2':data2,'data3':data3})


def show_page(request):
	data1 = Page.objects.all()
	data2 = Page.objects.filter(page_cat = 'Germany')
	data3 = Page.objects.filter(user__last_name = 'Ghimire')
	return render(request,'myapp/page.html',{'data1':data1,'data2':data2,'data3':data3})


def show_post(request):
	data1 = Post.objects.all()
	data2 = Post.objects.filter(post_publish_date='2022-04-20')
	data3 = Post.objects.filter(user__username='Niket')

	return render(request,'myapp/post.html',{'data1':data1,'data2':data2,'data3':data3})




def show_user(request):
	data1 = User.objects.all()
	#print(data1[1].last_name)
	data2 = User.objects.filter(last_name = 'Ghimire')
	data3 = User.objects.filter(page__page_cat='Germany')
	data4 = User.objects.filter(post__post_publish_date = '2022-04-20')
	data5 = User.objects.filter(song__song_duration=7)
	return render(request,'myapp/user.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})


def home(request):
	return render(request,'myapp/home.html')