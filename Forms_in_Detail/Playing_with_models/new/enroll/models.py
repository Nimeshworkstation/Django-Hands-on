from django.db import models

# Create your models here.

class Student(models.Model):
	stuid=models.IntegerField()
	stuname=models.CharField(max_length=70)
	studemail=models.EmailField(max_length=70)
	stupass=models.CharField(max_length=70)
	comment=models.CharField(max_length=40 , default='not available')

	def __str__(self):
		return self.stuname