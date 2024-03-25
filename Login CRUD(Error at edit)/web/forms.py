from django.forms  import ModelForm
from .models import Member

class empforms(ModelForm):
	class Meta:
		model= Member
		fields = '__all__'
