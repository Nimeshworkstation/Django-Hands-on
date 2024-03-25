from django.contrib import admin
from .models import Student

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
	list_display = ['id','name','roll','course']

# Register your models here.
