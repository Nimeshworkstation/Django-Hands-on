from django import forms


class StudentForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	first_name = forms.CharField() 
	mobile = forms.IntegerField()
	key = forms.CharField(widget=forms.HiddenInput())