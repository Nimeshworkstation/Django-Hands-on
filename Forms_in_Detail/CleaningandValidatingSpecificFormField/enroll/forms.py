from django import forms


class StudentForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	#validation for name field
	def clean_name(self):
		sname=self.cleaned_data['name']
		length = len(sname)
		if length == None or length == "":
			raise forms.ValidationError('Enter more than or equal to four character, this is my warning to you !!!')

		return sname


	
	