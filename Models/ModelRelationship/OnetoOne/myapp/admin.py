from django.contrib import admin
from .models import Page

# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ['user_id','page_name','page_cat','page_publish','']
