from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentDetails(admin.ModelAdmin):
	list_display=['id','stuid','stuname','studemail','stupass']
