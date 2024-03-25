from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ['id','name']

@admin.register(Album)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ['id','artist','name']

@admin.register(Song)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ['id','album','name']

