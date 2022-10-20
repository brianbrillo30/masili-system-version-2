from django.shortcuts import render, redirect, HttpResponse
from apps.UserPortal.models import BuildingPermit
from .forms import *
from project.utils import render_to_pdf
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def building_permit_module(request):
    if request.user.is_authenticated:
        return render(request, 'BuildingPermit/building_permit_module.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def building_permit_list(request):
    if request.user.is_authenticated:
        context = {'building_permit_list':BuildingPermit.objects.all().order_by('id')}
        return render(request, 'BuildingPermit/building_permit_list.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def edit_building_permit(request, id):
    if request.user.is_authenticated:
        building_permit = BuildingPermit.objects.get(pk=id)
        form = BuildingPermitForm(instance=building_permit)
        
        if request.method == 'POST':
            form = BuildingPermitForm(request.POST,instance=building_permit)
            if form.is_valid():
                form.save()
                return HttpResponse(status=204, headers={'HX-Trigger': 'BuildingPermitList'})

        context = {'form':form, 'disabledform':building_permit}
        return render(request, 'BuildingPermit/building_permit_form.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def generate_building_permit(request, id):
    if request.user.is_authenticated:
        template_name = "BuildingPermit/building_permit_pdf.html"
        building_permit = BuildingPermit.objects.get(pk=id)
        
        return render_to_pdf(
            template_name,
            {
                "building_permit": building_permit,
            },
        ) 
    else:
        return redirect('loginPage')


def delete_building_permit(request, id):
    if request.user.is_authenticated:
        building_permit = BuildingPermit.objects.get(pk=id)
        
        context = {'building_permit':building_permit}
        if request.method == 'POST':

            email_msg = request.POST.get('reason_masage')

            subject = 'Reasons For Denying your Request'
            message = email_msg
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [building_permit.res_id.user.email]
            send_mail( subject, message, email_from, recipient_list )

            building_permit.delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'BuildingPermitList'})
        return render(request, 'BuildingPermit/delete_building_permit.html', context)

    else:
        return redirect('loginPage')

    