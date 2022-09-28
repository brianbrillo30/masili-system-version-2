from django.shortcuts import render, HttpResponse
from apps.UserPortal.models import ResidencyCertificate
from .forms import *
from project.utils import render_to_pdf
# Create your views here.

def residency_certificate_module(request):
    return render (request, 'ResidencyCertificate/resident_certificate_module.html')

def residency_certificate_list(request):
    context = {'residency_certificate_list':ResidencyCertificate.objects.all().order_by('id')}
    return render(request, 'ResidencyCertificate/residency_certificate_list.html', context)

def edit_residency(request, id):
    residency_certificate = ResidencyCertificate.objects.get(pk=id)
    form = ResidencyCertificateForm(instance=residency_certificate)

    if request.method == 'POST':
        form = ResidencyCertificateForm(request.POST,instance=residency_certificate)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'ResidencyList'})

    context = {'form':form, 'disabledform':residency_certificate}
    return render(request, 'ResidencyCertificate/residency_certificate_form.html', context)

def generate_resident_certificate(request, id):

    template_name = "ResidencyCertificate/resident_certificate_pdf.html"
    residency_certificate = ResidencyCertificate.objects.get(pk=id)
    
    return render_to_pdf(
        template_name,
        {
            "residency_certificate": residency_certificate,
        },
    ) 
