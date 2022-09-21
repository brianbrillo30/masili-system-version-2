from atexit import register
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import unauthenticated_user, user_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.contrib.auth import logout, login, authenticate
# from django.contrib import messages
# from .decorators import unauthenticated_user

# Create your views here.

#@user_only
def home(request):
    return render(request, "UsersideTemplate/index.html")


#@user_only
def about(request):
     return render(request, "UsersideTemplate/about.html")


@unauthenticated_user
#@user_only
def userLogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        resident = authenticate(request, username = username, password = password )

        if not resident:
            messages.add_message(request, messages.ERROR, 'Invalid username or password !')
            return render(request, "UsersideTemplate/login.html")

        login(request, resident)

        return redirect(reverse('service_portal'))

    return render(request, "UsersideTemplate/login.html")
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="userLogin")
@user_only
def servicesPortal(request):
    if request.user.is_authenticated:
        return render(request, "UsersideTemplate/service_portal.html")
    else:
        return redirect('userLogin')


def userLogout(request):
     logout(request)
     return redirect(reverse('home'))




#     return render(request, "UsersideTemplate/login.html")
# def index(request):
#     return render(request, "UsersideTemplate/index.html")

# def about(request):
#     return render(request, "UsersideTemplate/about.html")

# def ServicesPortal(request):
#     return render(request, "UsersideTemplate/service_portal.html")

# def userLogout(request):
#     logout(request)
#     return redirect(reverse('index'))

# @unauthenticated_user
# def userLogin(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
            
#         resident = authenticate(request, username = username, password = password )

#         if not resident:
#             messages.add_message(request, messages.ERROR, 'Invalid username or password !')
#             return render(request, "UsersideTemplate/login.html")

#         login(request, resident)

#         return redirect(reverse('service_portal'))

def about(request):
    return render(request, "UsersideTemplate/about.html")

