from atexit import register
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

from apps.AnnouncementManagement.models import Announcement
from .forms import *
from .models import clearance as clr,CertificateOfIndigency as coi,BuildingPermit as buildingpermit, BusinessPermit as businesspermit, ResidencyCertificate as rescert

from django.contrib.auth.forms import UserChangeForm



# Create your views here.

def home(request):
    return render(request, "UsersideTemplate/index.html")


def about(request):
     return render(request, "UsersideTemplate/about.html")

def contact(request):
    return render(request, "UsersideTemplate/contact.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def servicesPortal(request):
    if request.user.is_authenticated:
        return render(request, "UsersideTemplate/service_portal.html")
    else:
        return redirect('loginPage')


def userLogout(request):
     logout(request)
     return redirect(reverse('home'))


def about(request):
    return render(request, "UsersideTemplate/about.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def barangay_clearance(request):
    if request.user.is_authenticated:
        form = CleranceForm
        userid = request.user.residentsinfo
        if request.method == 'POST':
            form = CleranceForm(request.POST)
            if form.is_valid():
                docs = clearance.objects.filter(res_id=userid)
                if docs.get(status=1):
                    messages.success(request, 'You still have pending request')
                    return redirect('service_portal')
                else:
                    instance = form.save(commit=False)
                    instance.res_id = userid
                    instance.save()
                    messages.success(request, 'Your request has been submitted. You can see your request status at Document Status')
                    return redirect('service_portal')

        context={'form':form} 
        return render(request, "UsersideTemplate/barangay_clearance.html", context)
    else:
        return redirect('loginPage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def indigency(request):
    if request.user.is_authenticated:
        form = IndigencyForm
        userid = request.user.residentsinfo
        if request.method == 'POST':
            form = IndigencyForm(request.POST)
            if form.is_valid():
                
                
                instance = form.save(commit=False)
                instance.res_id = userid
                instance.save()
                messages.success(request, 'Your request has been submitted. You can see your request status at Document Status')
                return redirect('service_portal')
        context={'form':form} 
        return render(request, "UsersideTemplate/indigency.html", context)
    else:
        return redirect('loginPage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def BuildingPermit(request):
    if request.user.is_authenticated:
        form = BuildingPermitForm
        userid = request.user.residentsinfo
        if request.method == 'POST':
            form = BuildingPermitForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.res_id = userid
                instance.save()
                messages.success(request, 'Your request has been submitted. You can see your request status at Document Status')
                return redirect('service_portal')

        context={'form':form}
        return render(request, "UsersideTemplate/building_permit.html", context)
    else:
        return redirect('loginPage')    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def BusinessPermit(request):
    if request.user.is_authenticated:
        form = BusinessPermitForm
        userid = request.user.residentsinfo
        if request.method == 'POST':
            form = BusinessPermitForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.res_id = userid
                instance.save()
                messages.success(request, 'Your request has been submitted. You can see your request status at Document Status')
                return redirect('service_portal')
        context={'form':form}
        return render(request, "UsersideTemplate/business_permit.html", context)
    else:
        return redirect('loginPage') 

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def ResidencyCertificate(request):
    if request.user.is_authenticated:
        form = ResidencyCertificateForm
        userid = request.user.residentsinfo
        if request.method == 'POST':
            form = ResidencyCertificateForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.res_id = userid
                instance.save()
                messages.success(request, 'Your request has been submitted. You can see your request status at Document Status')
                return redirect('service_portal')
        context={'form':form}
        return render(request, 'UsersideTemplate/residency_certificate.html', context)
    else:
        return redirect('loginPage') 


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'UsersideTemplate/profile.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def changeEmail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateEmailForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your email has been updated')
                return redirect('profile')
        else:
            form = UpdateEmailForm(instance=request.user)
            context = {'form': form}
        return render(request, 'UsersideTemplate/change_email.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
def changeUsername(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateUsernameForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your username has been updated')
                return redirect('profile')
        else:
            form = UpdateUsernameForm(instance=request.user)
            context = {'form': form}
        return render(request, 'UsersideTemplate/change_username.html', context)
    else:
        return redirect('loginPage')

def announce(request):
    announce_list = Announcement.objects.all()
    context = {'announcementList' :  announce_list}
    return render(request, 'UsersideTemplate/announcement.html', context)



def document_status(request):
    

    user_id = request.user.residentsinfo.id
    clearance_status = clr.objects.filter(res_id=user_id)
    indigency_status = coi.objects.filter(res_id=user_id)
    business_status =   businesspermit.objects.filter(res_id=user_id)
    building_status = buildingpermit.objects.filter(res_id=user_id)
    residency_status = rescert.objects.filter(res_id=user_id)
    context = {
        'clearance_list': clearance_status, 
        'indigency_list': indigency_status,
        'business_list' : business_status,
        'building_list' : building_status,
        'residency_list': residency_status
    }
    return render(request, 'UsersideTemplate/doc_status.html', context)
    