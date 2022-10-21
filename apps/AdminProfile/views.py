from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from apps.UserPortal.forms import *
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def adminProfile(request):
    if request.user.is_authenticated:
        return render(request, 'AdminProfile/admin_profile.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def changeUsernameAdmin(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateUsernameForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your username has been updated')
                return redirect('adminProfile')
            else:
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == 'This field is required.':
                        messages.error(request, "You must pass the reCAPTCHA test")
                        continue
                
                    messages.error(request, error) 

        form = UpdateUsernameForm(instance=request.user)
        context = {'form': form}
        return render(request, 'AdminProfile/change_username.html', context)
    else:
        return redirect('loginPage')



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def changeEmailAdmin(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateEmailForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your email has been updated')
                return redirect('adminProfile')
            else:
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == 'This field is required.':
                        messages.error(request, "You must pass the reCAPTCHA test")
                        continue
                
                    messages.error(request, error) 

        form = UpdateEmailForm(instance=request.user)
        context = {'form': form}
        return render(request, 'AdminProfile/change_email.html', context)
    else:
        return redirect('loginPage')
