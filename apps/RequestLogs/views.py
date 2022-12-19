from django.shortcuts import render, redirect
from apps.UserPortal.models import *
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only

def requestLogs(request):
    if request.user.is_authenticated:
        clearance_list = clearance.objects.all()
        indigency_list = CertificateOfIndigency.objects.all()
        business_list = BusinessPermit.objects.all()
        building_list = BuildingPermit.objects.all()
        residency_list = ResidencyCertificate.objects.all()
        context = {
            'clearance_list': clearance_list, 
            'indigency_list': indigency_list,
            'business_list' : business_list,
            'building_list' : building_list,
            'residency_list': residency_list
        }
        return render (request, 'RequestLogs/requested_document_logs.html', context )
    else:
        return redirect('loginPage')