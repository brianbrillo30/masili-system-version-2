from django.shortcuts import render
from apps.ResidentManagement.models import ResidentsInfo
# Create your views here.

def reports(request):
    return render (request, 'ReportManagement/reports.html')

# def reports(request):
#     report_list = ResidentsInfo.objects.select_related('clearance', 'CertificateOfIndigency', 'BuildingPermit')
#     context = {'reports':report_list}
#     return render (request, 'ReportManagement/reports.html', context)