from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

                group = None
                if request.user.groups.exists():
                 group = request.user.groups.all()[0].name
            #    print('it is working', allowed_roles)
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs);
                else:
                    return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def admins_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':   
            return redirect('user_profile') # if the user is customer  it is going to be redirected to user-page..
        elif group == 'admin':
            return view_func(request, *args,** kwargs ) # if a user is admin allows to  be in the page
        
    return wrapper_function