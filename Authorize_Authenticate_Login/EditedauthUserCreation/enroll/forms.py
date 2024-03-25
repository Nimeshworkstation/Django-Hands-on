from django.contrib.auth.models import User # import user class 
from django.contrib.auth.forms import UserCreationForm 
from django import forms
# import usercreationform

class SignupForm(UserCreationForm):
	password2 = forms.CharField(label='Confirm Password (again)', widget = forms.PasswordInput)
	class Meta:
		model = User # it is inherited from djano.contrib.auth.models import USER
		fields = ['username', 'first_name', 'last_name', 'email'] # it is from UsercreationForm
		labels={'email':'Email', 'first_name':'FirstName','last_name':'LastName'} # it changes the default label name provided by django usercreationform