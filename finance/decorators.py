# a decorator is a function that takes another function as a parameter and let us add extra functionality 
# before original function is called
#  decorators can be used to restrict access to certain views.
#  Django come with some built-in decorators, like login_required , require_POST or has_permission 
from django.http import HttpResponse
from django.shortcuts import redirect
def unauthenticated_user(view_fun):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_fun(request,*args,**kwargs)
    return wrapper_func