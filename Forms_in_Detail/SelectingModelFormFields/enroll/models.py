from django.db import models

class User(models.Model):
	name = models.CharField(max_length = 70, blank = True)
	email=models.EmailField(max_length = 70)
	password = models.CharField(max_length = 70)
