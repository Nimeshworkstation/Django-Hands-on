from django import forms


class StudentForm(forms.Form):
	name = forms.CharField()
	name1 = forms.CharField(widget=forms.PasswordInput())
	name2 = forms.CharField(widget=forms.HiddenInput())
	name3 = forms.CharField(widget=forms.Textarea())
	name4 = forms.CharField(widget=forms.CheckboxInput())
	name5 = forms.CharField(widget=forms.FileInput())
	name6 = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss'}))

	