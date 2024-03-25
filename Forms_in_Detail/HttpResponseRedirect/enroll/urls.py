from django.urls import path
from enroll import views

urlpatterns = [
path('',views.AddStudent, name = 'viewstudent'),
path('success/',views.thankyou, name = 'success'),
]