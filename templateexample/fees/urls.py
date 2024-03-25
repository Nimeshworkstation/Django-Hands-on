from django.urls import path
from  fees import views

urlpatterns = [
	path('',views.feesInfo, name = 'courseInfo'),
]