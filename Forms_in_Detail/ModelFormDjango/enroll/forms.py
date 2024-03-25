from django import forms
from django.core import validators	
from . models import User	

class StudentForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name','email','password']
		labels = {'name':'Enter Name','password':'Enter password','email':'Enter Email'}
		help_text = {'email':'Enter your Full Name'}
		error_messages = {
			'email':{'required': 'email lekh muji',
				},
			'password':{
					'required':'password lekh chikne',
				},
			}
		widgets = {
			'password':forms.PasswordInput,
			'name':forms.TextInput(attrs={'class': 'myclass', 'placeholder':'ya naam lekh jatho'})
		}

	