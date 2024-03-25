from django import forms


class StudentForm(forms.Form):
	uname = forms.CharField()
	email = forms.EmailField()
	first_name = forms.CharField()