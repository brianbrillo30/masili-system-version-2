from django.shortcuts import render, redirect
from apps.UserPortal.models import *
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only

def reports(request):
    if request.user.is_authenticated:
        clearance_list = clearance.objects.filter(status=3)
        indigency_list = CertificateOfIndigency.objects.filter(status=3)
        business_list = BusinessPermit.objects.filter(status=3)
        building_list = BuildingPermit.objects.filter(status=3)
        residency_list = ResidencyCertificate.objects.filter(status=3)
        context = {
            'clearance_list': clearance_list, 
            'indigency_list': indigency_list,
            'business_list' : business_list,
            'building_list' : building_list,
            'residency_list': residency_list
        }
        return render (request, 'ReportManagement/reports.html', context)
    else:
        return redirect('loginPage')


def clearance_reports(request):
    if request.user.is_authenticated:
        clearance_list = clearance.objects.filter(status=3)
        context = {
            'clearance_list': clearance_list
        }
        return render (request, 'ReportManagement/clearance_reports.html', context)
    else:
        return redirect('loginPage')


def indigency_reports(request):
    if request.user.is_authenticated:
        indigency_list = CertificateOfIndigency.objects.filter(status=3)
        context = {
            'indigency_list': indigency_list
        }
        return render (request, 'ReportManagement/indigency_reports.html', context)
    else:
        return redirect('loginPage')

def business_reports(request):
    if request.user.is_authenticated:
        business_list = BusinessPermit.objects.filter(status=3)
        context = {
            'business_list' : business_list
        }
        return render (request, 'ReportManagement/business_reports.html', context)
    else:
        return redirect('loginPage')


def building_reports(request):
    if request.user.is_authenticated:
        building_list = BuildingPermit.objects.filter(status=3)
        context = {
            'building_list' : building_list,
        }
        return render (request, 'ReportManagement/building_reports.html', context)
    else:
        return redirect('loginPage')


def residency_reports(request):
    if request.user.is_authenticated:
        residency_list = ResidencyCertificate.objects.filter(status=3)
        context = {
            'residency_list': residency_list
        }
        return render (request, 'ReportManagement/residency_reports.html', context)
    else:
        return redirect('loginPage')

