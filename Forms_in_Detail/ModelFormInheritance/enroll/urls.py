from django.urls import path
from enroll import views

urlpatterns = [
path('student/',views.student_form, name = 'student'),
path('teacher/',views.teacher_form, name = 'teacher')
]