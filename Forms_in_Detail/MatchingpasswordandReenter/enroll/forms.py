from django import forms
from django.core import validators		
def emailstarts_with_n(value):
	if value[0] != 'n':
		raise forms.ValidationError('It should starts with n')


class StudentForm(forms.Form):
	name = forms.CharField(validators=[validators.MaxLengthValidator(10),emailstarts_with_n])
	email = forms.EmailField(validators=[emailstarts_with_n])
	password = forms.CharField(widget=forms.PasswordInput)
	rpassword = forms.CharField(widget=forms.PasswordInput,label='Password(again)')

	def clean(self):
		cleaned_data = super().clean()
		valpwd = self.cleaned_data['password']
		valrpwd = self.cleaned_data['rpassword']
		if valpwd != valrpwd:
			raise forms.ValidationError('password does not match')

	

	
	