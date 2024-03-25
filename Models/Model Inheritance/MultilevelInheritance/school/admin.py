from django.contrib import admin
from .models import Student, ExamCenter

# Register your models here.
# Register your models here.
# Register your models here.
@admin.register(ExamCenter)
class ExamCenterData(admin.ModelAdmin):
	list_display=['id','cname','city']

@admin.register(Student)
class StudentData(admin.ModelAdmin):
	list_display=['id','cname','city','name','roll']