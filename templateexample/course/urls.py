from django.urls import path
from course import views

urlpatterns = [
	path('',views.courseInfo, name = 'courseInfo'),
]