from django.shortcuts import HttpResponse
class MyProcessExceptionMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resonse = self.get_response(request)
        return resonse

    def process_exception(self, request, exception):
        msg = exception
        print("Exception Occured ")
        return HttpResponse(msg)