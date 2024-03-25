from django import forms
from django.core import validators		
def emailstarts_with_n(value):
	if value[0] != 'n':
		raise forms.ValidationError('It should starts with n')


class StudentForm(forms.Form):
	name = forms.CharField(validators=[validators.MaxLengthValidator(10),emailstarts_with_n])
	email = forms.EmailField(validators=[emailstarts_with_n])
	password = forms.CharField(widget=forms.PasswordInput)

	

	
	