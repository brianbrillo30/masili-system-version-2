from django.shortcuts import render, redirect, HttpResponse
from apps.UserPortal.models import BusinessPermit 
from .forms import *
from project.utils import render_to_pdf
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def business_permit_module(request):
    if request.user.is_authenticated:
        return render (request, 'BusinessPermit/business_permit_module.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def business_permit_list(request):
    if request.user.is_authenticated:
        context = {'business_permit_list' : BusinessPermit.objects.all().order_by('id')}
        return render(request, 'BusinessPermit/business_permit_list.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def edit_business_permit(request, id):
    if request.user.is_authenticated:
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
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def generate_business_permit(request, id):
    if request.user.is_authenticated:
        template_name = "BusinessPermit/business_permit_pdf.html"
        business_permit = BusinessPermit.objects.get(pk=id)
        
        return render_to_pdf(
            template_name,
            {
                "business_permit": business_permit,
            },
        )
    else:
        return redirect('loginPage')