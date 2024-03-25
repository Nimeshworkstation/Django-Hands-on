from django import forms


class StudentForm(forms.Form):
	name = forms.CharField(label='Your Name') #changing Label Name
	name1 = forms.CharField(label='Your Name', label_suffix='') # Removing colon from Label
	name2 = forms.CharField(label='Your Name', label_suffix='',initial='Nimesh') #setting initial Value
	name3 = forms.CharField(label='Your Name', label_suffix='',initial='Nimesh', required=False) # setting required value to True or FAlse
	name4 = forms.CharField(label='Your Name', label_suffix='',initial='Nimesh', required=False, disabled=True) # making the field disabled or not
	name5 = forms.CharField(label='Your Name', label_suffix='',initial='Nimesh', required=False, help_text='Limit 70 Char') #Providing help text