from django.urls import path
from student import views

urlpatterns = [
path('set/',views.setcookie,name = 'setcookie'),
path('get/',views.getcookie,name = 'getcookie'),
path('del/',views.delcookie,name = 'deletecookie'),
]