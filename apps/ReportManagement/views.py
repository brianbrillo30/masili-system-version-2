from django.shortcuts import render
from apps.UserPortal.models import *
# Create your views here.

def reports(request):
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



