from django import forms


class StudentForm(forms.Form):
	name = forms.CharField(initial='Nimesh',help_text="yo field ma 30 character matrai haalna milchha for example")
	email = forms.EmailField()
	first_name = forms.CharField() 