from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            view_func(request, *args, **kwargs)

    return wrapper

def allowed_user(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs);
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorators
def admins_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0]
        
        if group == 'customer':   
            return redirect('user-page') # if the user is customer  it is going to be redirected to user-page..
        if group == 'admin':
            return view_func(request, *args,** kwargs ) # if a user is admin allows to  be in the page

    return wrapper_func