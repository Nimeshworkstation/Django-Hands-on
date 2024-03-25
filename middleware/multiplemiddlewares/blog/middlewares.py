from django.shortcuts import HttpResponse
class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("One-time Brother Intialization Started....")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("This is Brother before View")
        print("-----------------------")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("This is Brother after View")
        print("------------------------")

        return response



class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("One-time Father Intialization Started....")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("This is Father before View")
        print("--------------------------")

        #response = self.get_response(request)
        response = HttpResponse("pehli Furst mein Nikl ")

        # Code to be executed for each request/response after
        # the view is called.
        print("This is Father after View")
        print("--------------------------")

        return response



class MummyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("One-time Mummy Intialization Started....")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("This is Mummy before View")


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("This is Mummy after View")

        return response



