from django import forms
from . models import User

class StudentReg(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'