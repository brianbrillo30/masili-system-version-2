from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('resident_list')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            
            group = request.user.groups.all()[0].name
            
        if group == 'resident':
        
            return redirect('service_portal')
            #return HttpResponse('YOU ARE NOT AUTHORIZED TO ACCESS THIS PAGE! PLEASE CLICK <a href="http://127.0.0.1:8000/Barangay Masili/User Logout">Here</a>')
            #messages.success(request, 'Invalid username or password')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function