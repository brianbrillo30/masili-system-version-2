from atexit import register
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import unauthenticated_user
from django.views.decorators.cache import cache_control

# Create your views here.


def home(request):
    return render(request, "UsersideTemplate/index.html")

@unauthenticated_user
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
def servicesPortal(request):
    if request.user.is_authenticated:
        return render(request, "UsersideTemplate/service_portal.html")
    else:
        return redirect('userLogin')

def userLogout(request):
     logout(request)
     return redirect(reverse('home'))

def about(request):
    return render(request, "UsersideTemplate/about.html")

