from django.shortcuts import render, HttpResponse, redirect
from apps.UserPortal.models import clearance as clerance_list
from .forms import *
from project.utils import render_to_pdf
# Create your views here.

def clearance(request):
    return render(request, 'ClearanceManagement/clearance_table.html')

def clearance_list(request):
    context = {'clearance_list' :  clerance_list.objects.all().order_by('id')}
    return render(request, 'ClearanceManagement/clearance_list.html', context)


def edit_clearance(request, id):

    clearance = clerance_list.objects.get(pk=id)
    form = cleranceForm(instance=clearance)

    clearance_id = clerance_list.objects.get(pk=id)
    if request.method == 'POST':
        form = cleranceForm(request.POST,instance=clearance)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'clearancelistUpdate'})


    context = {'form':form, 'disabledform':clearance_id}
    return render(request, 'ClearanceManagement/clearance_form.html', context)

def generate_clearance (requesr, id):
    
    template_name = "ClearanceManagement/clearance_pdf.html"
    clearance = clerance_list.objects.get(pk=id)
    
    return render_to_pdf(
        template_name,
        {
            "clearance": clearance,
        },
    )


