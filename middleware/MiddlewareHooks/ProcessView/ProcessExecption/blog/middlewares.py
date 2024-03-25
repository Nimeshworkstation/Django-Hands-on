from django.shortcuts import HttpResponse
class MyProcessMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resonse = self.get_response(request)
        return resonse

    def process_view(request, *args, **kwargs):
        ''' If HttpResponse is returned from middlewares then
        view is not called, response is retruned from middleware.If 
        none is passed here, then only view is called.'''
        #return HttpResponse("This is before View")
        None