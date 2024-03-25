from django import forms
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	'''#validation for name field
	def clean_name(self):
		name=self.cleaned_data['name']
		if len(name)<4:
			raise forms.ValidationError('Enter more than or equal to four character, this is my warning to you !!!')
		return name'''

	def clean(self):
		cleaned_data = super().clean()
		valname = self.cleaned_data['name']
		valemail = self.cleaned_data['email']
		if len(valname) <4:
			raise forms.ValidationError('Enter more than 4')


		if len(valemail)<6:
			raise forms.ValidationError('Enter more than 10')


	
	