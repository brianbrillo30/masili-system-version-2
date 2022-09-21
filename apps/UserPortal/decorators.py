from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('service_portal')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def user_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return redirect('resident_list')

        if group == 'resident':
            return view_func(request, *args, **kwargs)

    return wrapper_function
