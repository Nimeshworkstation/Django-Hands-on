from django.shortcuts import HttpResponse
class MyProcessTemplateMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resonse = self.get_response(request)
        return resonse

    def process_template_response(self, request, response):
        print("Process Template Respnose From Middleware")
        response.context_data['name'] = 'Sonam'
        return response