def my_middleware(get_response):
    # One-time configuration and initialization.
    print ("One-time Configuration and initialization!!")

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("This is before view")

        response = get_response(request)

        print("This is after view")

        # Code to be executed for each request/response after
        # the view is called.

        return response
    return middleware


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("One-time Intialization Started....")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("This is before View")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("This is after View")

        return response
