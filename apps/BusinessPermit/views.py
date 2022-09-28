from django.shortcuts import render, HttpResponse
from apps.UserPortal.models import BusinessPermit 
from .forms import *
from project.utils import render_to_pdf
# Create your views here.

def business_permit_module(request):
    return render (request, 'BusinessPermit/business_permit_module.html')

def business_permit_list(request):
    context = {'business_permit_list' : BusinessPermit.objects.all().order_by('id')}
    return render(request, 'BusinessPermit/business_permit_list.html', context)

def edit_business_permit(request, id):
    business_permit = BusinessPermit.objects.get(pk=id)
    form = BusinessPermitForm (instance=business_permit)

    business_permit_id = BusinessPermit.objects.get(pk=id)
    if request.method == 'POST':
        form = BusinessPermitForm(request.POST,instance=business_permit)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'BusinessPermitlistUpdate'})

    context = {'form':form, 'disabledform':business_permit_id}
    return render(request, 'BusinessPermit/business_permit_form.html', context)

def generate_business_permit(request, id):

    template_name = "BusinessPermit/business_permit_pdf.html"
    business_permit = BusinessPermit.objects.get(pk=id)
    
    return render_to_pdf(
        template_name,
        {
            "business_permit": business_permit,
        },
    )