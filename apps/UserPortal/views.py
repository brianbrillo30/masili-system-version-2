from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .decorators import unauthenticated_user
# Create your views here.

def index(request):
    return render(request, "UsersideTemplate/index.html")

def about(request):
    return render(request, "UsersideTemplate/about.html")

def ServicesPortal(request):
    return render(request, "UsersideTemplate/service_portal.html")

@unauthenticated_user
def userLogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        resident = authenticate(request, username = username, password = password )

        if not resident:
            messages.add_message(request, messages.ERROR, 'Invalid username or password !')
            return render(request, "login.html")

        login(request, resident)

        return redirect(reverse('resident_list'))

    return render(request, "UsersideTemplate/login.html")

def services(request):
    return render(request, "UsersideTemplate/services.html")
