from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

#The first way to do is as shown in this class
#using @method_decorator and dispatch method

class ProfileTemplateView(TemplateView):
	template_name  = 'registration/profile.html'
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)




#The second way is to do this is as shown here by putting 
#all inside @method_decorator.

@method_decorator(staff_member_required, name = 'dispatch')
class AboutTemplateView(TemplateView):
	template_name  = 'registration/about.html'