from django.contrib import admin
from .models import Student, Teacher, Contractor

# Register your models here.
@admin.register(Student)
class StudentData(admin.ModelAdmin):
	list_display=['id','name','age','fees']

@admin.register(Teacher)
class TeacherData(admin.ModelAdmin):
	list_display=['id','name','age','date','salary']

@admin.register(Contractor)
class ContractorData(admin.ModelAdmin):
	list_display=['id','name','age','date','payment']