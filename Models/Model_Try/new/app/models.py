from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
    	return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    def __str__(self):
    	return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    def __str__(self):
    	return self.name
