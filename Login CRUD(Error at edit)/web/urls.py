from django.urls import path

from . import views

urlpatterns = [
	path('index/',views.index, name='index'),
	path('login/',views.login, name='login'),
	path('home/', views.home , name= 'home'),
	path('main/', views.main, name='main'),
	path('detail/', views.detail, name = 'detail'),
	path('edit/<int:id>/',views.edit, name = 'edit'),
	path('update/<int:id>/',views.update, name = 'update'),
]