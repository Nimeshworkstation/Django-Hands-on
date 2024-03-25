from django.urls import path
from student import views

urlpatterns = [
	path('set/',views.settestcookie),
	path('check/',views.checktestcookie),
	path('del/',views.deltestcookie),
]