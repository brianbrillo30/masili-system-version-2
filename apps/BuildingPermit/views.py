from django.shortcuts import render, HttpResponse
from apps.UserPortal.models import BuildingPermit
from .forms import *
# Create your views here.

def building_permit_module(request):
    return render(request, 'BuildingPermit/building_permit_module.html')

def building_permit_list(request):
    context = {'building_permit_list':BuildingPermit.objects.all().order_by('id')}
    return render(request, 'BuildingPermit/building_permit_list.html', context)

def edit_building_permit(request, id):
    building_permit = BuildingPermit.objects.get(pk=id)
    form = BuildingPermitForm(instance=building_permit)
    
    if request.method == 'POST':
        form = BuildingPermitForm(request.POST,instance=building_permit)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'BuildingPermitList'})

    context = {'form':form, 'disabledform':building_permit}
    return render(request, 'BuildingPermit/building_permit_form.html', context)

    