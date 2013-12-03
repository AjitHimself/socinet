from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from functools import wraps

def check_user(session_key):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            if request.session.get(session_key):
                return func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('users.views.login'))

        return wraps(func)(inner_decorator)

    return decorator