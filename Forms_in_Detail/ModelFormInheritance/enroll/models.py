from django.db import models

class User(models.Model):
	student_name = models.CharField(max_length = 70, null = True)
	teacher_name = models.CharField(max_length= 70,null = True)
	email=models.EmailField(max_length = 70)
	password = models.CharField(max_length = 70)
