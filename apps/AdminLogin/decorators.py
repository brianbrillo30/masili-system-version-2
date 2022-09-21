from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('resident_list')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            
            group = request.user.groups.all()[0].name
            
        if group == 'resident':
            #return redirect('service_portal')
            return HttpResponse('YOU ARE NOT AUTHORIZED TO ACCESS THIS PAGE! PLEASE CLICK <a href="http://127.0.0.1:8000/Barangay Masili/User Logout">Here</a>')
            #messages.success(request, 'Invalid username or password')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function