from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .decorators import unauthenticated_user


# Create your views here.


@unauthenticated_user
def loginPage(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        user = authenticate(request, username = username, password = password )

        if not user:
            messages.add_message(request, messages.ERROR, 'Invalid username or password !')
            return render(request, "Login/login.html")

        login(request, user)

        return redirect(reverse('dashboard'))

    return render(request, "Login/login.html")
    