from django import forms
from django.core import validators		

class StudentForm(forms.Form):
	error_css_class='error'
	required_css_class='required'
	name = forms.CharField(error_messages={'required':'Enter your Name'},label_suffix="")
	email = forms.EmailField(error_messages={'required':'Enter your Email'},label='Your Email',min_length=5,max_length=50, help_text='Limit 70 Char')
	password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your Password'},label="Password")
	
	
	