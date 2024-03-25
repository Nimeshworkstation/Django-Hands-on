from django import forms


class StudentForm(forms.Form):
	name = forms.CharField(min_length = 5)
	name1 = forms.CharField(min_length = 5, max_length = 10)
	name3 = forms.CharField(min_length = 5, max_length = 10, strip = False) ## allows spaces while input
	name4 = forms.CharField(empty_value='Nimesh',initial=' here initial value is submitted when field is empty submitted, No required error becase there is empty_value provided in forms.py') #passing an empty value when field is empty submitted
	name5 = forms.CharField(error_messages={'required':'This is edited error message'}) #replaces required error message with our message


	roll = forms.IntegerField(min_value=5, max_value=50000)

	price = forms.DecimalField(min_value=5, max_value=40, max_digits=6, decimal_places=1)

	rate = forms.FloatField(min_value=5, max_value=5000)

	comment = forms.SlugField()
	email = forms.EmailField(min_length=5, max_length=50)
	website=forms.URLField(min_length = 5, max_length=50)
	password = forms.CharField(min_length=5,max_length=50,widget=forms.PasswordInput)
	description = forms.CharField(widget=forms.Textarea)
	feedback = forms.CharField(min_length=5, max_length=1000,widget=forms.TextInput(attrs={'class': 'somecss','id':'uniqueid'}))
	notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))

	agree = forms.BooleanField(label="I Agree",label_suffix='',required=False) # can be checked or unchecked 
	agree1 = forms.BooleanField(label="I Agree",label_suffix='')# should be checked alwyas