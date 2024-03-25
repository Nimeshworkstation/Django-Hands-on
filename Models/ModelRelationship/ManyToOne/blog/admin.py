from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['user_id','id','post_title','post_cat','post_publish_date','user']

# Register your models here.
