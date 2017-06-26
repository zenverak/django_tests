from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.valid_paths = ['/', '/login/','/signup/']

    def process_view(self, request):
        header_token = request.META.get('HTTP_AUTHORIZATION', None)
        if header_token is not None:
          try:
            token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
            token_obj = Token.objects.get(key = token)
            request.user = token_obj.user
          except Token.DoesNotExist:
            pass
        #This is now the correct user
        print (request.user)
        return request


    def __call__(self, request):
        print "before process view"
        print "request is {0}".format(request)
        print "user is {0}".format(request.user)
        print "chached is {0}".format(request._cached_user)
        request = self.process_view(request)
        print "AFTER PROCESS VIEW"
        print "request is {0}".format(request)
        print "user is {0}".format(request.user)
        print "chached is {0}".format(request._cached_user)

        #response = self.get_response(request)
        print "RESPONSE is {0}".format(response)
        print "user is authenticated is {0}".format(request.user.is_authenticated())
        if not request.user.is_authenticated():
            if not request.path in self.valid_paths:
                return HttpResponseRedirect('/')

        # Code to be executed for each request/response after
        # the view is called.

        return response
