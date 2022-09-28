from django.shortcuts import redirect


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            
            group = request.user.groups.all()[0].name
            
        if group == 'resident':
        
            return redirect('service_portal')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function