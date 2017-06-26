from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.valid_paths = ['/', '/login/','/signup/']

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print request.path
##        try:
##            print "reverse is {0}".format(reverse('/'))
##        except:
##            print 'oops'

        response = self.get_response(request)
        print "user is authenticated is {0}".format(request.user.is_authenticated())
        if not request.user.is_authenticated():
            if not request.path in self.valid_paths:
                return HttpResponseRedirect('/')

        # Code to be executed for each request/response after
        # the view is called.

        return response
