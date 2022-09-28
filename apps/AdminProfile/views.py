from django.shortcuts import render, redirect
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def adminProfile(request):
    if request.user.is_authenticated:

        return render(request, 'AdminProfile/admin_profile.html')
    
    else:
        return redirect('loginPage')
