from django.contrib import admin
from .models import Post, Page, Song
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ['user_id','page_name','page_cat','page_publish_date','user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id','post_title','post_cat','post_publish_date','user']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ['id','song_name','song_duration','written_by']