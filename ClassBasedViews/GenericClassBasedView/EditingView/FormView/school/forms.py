from django import forms

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	msg = forms.CharField(widget = forms.Textarea)



class UpdateForm(forms.Form):
	Rename = forms.CharField()
	Reemail = forms.EmailField()
	Remsg = forms.CharField(widget = forms.Textarea)