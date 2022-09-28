from atexit import register
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import unauthenticated_user, user_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

def home(request):
    return render(request, "UsersideTemplate/index.html")


def about(request):
     return render(request, "UsersideTemplate/about.html")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
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

def barangay_clearance(request):

    form = CleranceForm
    userid = request.user.residentsinfo
    if request.method == 'POST':
        form = CleranceForm(request.POST)
        if form.is_valid():
            
            instance = form.save(commit=False)
            instance.res_id = userid
            instance.save()
            return redirect('service_portal')

    context={'form':form} 
    return render(request, "UsersideTemplate/barangay_clearance.html", context)


def indigency(request):
    form = IndigencyForm
    userid = request.user.residentsinfo
    if request.method == 'POST':
        form = IndigencyForm(request.POST)
        if form.is_valid():
            
            instance = form.save(commit=False)
            instance.res_id = userid
            instance.save()
            return redirect('service_portal')
    context={'form':form} 
    return render(request, "UsersideTemplate/indigency.html", context)


def BuildingPermit(request):
    form = BuildingPermitForm
    userid = request.user.residentsinfo
    if request.method == 'POST':
        form = BuildingPermitForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.res_id = userid
            instance.save()
            return redirect('service_portal')

    context={'form':form}
    return render(request, "UsersideTemplate/building_permit.html", context)

def BusinessPermit(request):

    form = BusinessPermitForm
    userid = request.user.residentsinfo
    if request.method == 'POST':
        form = BusinessPermitForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.res_id = userid
            instance.save()
            return redirect('service_portal')
    context={'form':form}
    return render(request, "UsersideTemplate/business_permit.html", context)


def ResidencyCertificate(request):
    form = ResidencyCertificateForm
    userid = request.user.residentsinfo
    if request.method == 'POST':
        form = ResidencyCertificateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.res_id = userid
            instance.save()
            return redirect('service_portal')
    context={'form':form}
    return render(request, 'UsersideTemplate/residency_certificate.html', context)