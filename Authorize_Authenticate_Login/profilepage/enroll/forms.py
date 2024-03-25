from django.contrib.auth.models import User # import user class 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
# import usercreationform

class SignupForm(UserCreationForm):
	password2 = forms.CharField(label='Confirm Password (again)', widget = forms.PasswordInput) # Password field is included in UserCreationForm so we can use it from here and don't need to display in User Class Fields 
	class Meta:
		model = User # it is inherited from djano.contrib.auth.models import USER
		fields = ['username', 'first_name', 'last_name', 'email'] 
		labels={'email':'Email', 'first_name':'FirstName','last_name':'LastName'} # it changes the default label name provided by django usercreationform


class EditUserProfileForm(UserChangeForm):
	password = None # It comes from UserChangeForm by default so we don't need to call it in User class
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','date_joined','last_login']
