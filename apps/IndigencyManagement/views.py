from django.shortcuts import render, HttpResponse
from apps.UserPortal.models import CertificateOfIndigency
from .forms import *
from .utils import render_to_pdf
# Create your views here.

def indigency_module(request):
    return render (request, 'IndigencyManagement/indigency_module.html')


def indigency_list(request):
    context = {'indigency_list' :  CertificateOfIndigency.objects.all().order_by('id')}
    return render(request, 'IndigencyManagement/indigency_list.html', context)

def edit_indigency(request, id):
    indigency = CertificateOfIndigency.objects.get(pk=id)
    form = indigencyForm(instance=indigency)

    indigency_id = CertificateOfIndigency.objects.get(pk=id)
    if request.method == 'POST':
        form = indigencyForm(request.POST,instance=indigency)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'indigencylistUpdate'})


    context = {'form':form, 'disabledform':indigency_id}
    return render(request, 'IndigencyManagement/indigency_form.html', context)


def generate_indigency (request, id):
    
    template_name = "IndigencyManagement/indigency_pdf.html"
    indigency = CertificateOfIndigency.objects.get(pk=id)
    
    return render_to_pdf(
        template_name,
        {
            "indigency": indigency,
        },
    )
