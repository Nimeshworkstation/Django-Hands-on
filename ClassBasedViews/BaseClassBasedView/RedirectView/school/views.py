from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.

class YoutubeRedirectView(RedirectView):
	url = 'https://www.youtube.com'



class YouRedirectView(RedirectView):
	pattern_name = 'mhome'
	permanent = True
	query_set = True

	def get_redirect_url(self, *args, **kwargs):
		print(kwargs)
		kwargs['pk'] = 55
		return super().get_redirect_url(*args, **kwargs)


		