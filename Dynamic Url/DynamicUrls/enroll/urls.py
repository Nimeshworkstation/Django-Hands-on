from django.urls import path
from enroll import views

urlpatterns = [
	path('',views.home,name = 'home'),
	path('<int:roll>/',views.show_details, name='show'),
	path('<int:roll>/<int:sub>/',views.show_subdetails, name='sub'),
]