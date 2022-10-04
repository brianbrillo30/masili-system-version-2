from django.shortcuts import render, redirect, HttpResponse
from apps.UserPortal.models import CertificateOfIndigency
from .forms import *
from project.utils import render_to_pdf
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def indigency_module(request):
    if request.user.is_authenticated:
        return render (request, 'IndigencyManagement/indigency_module.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def indigency_list(request):
    if request.user.is_authenticated:
        context = {'indigency_list' :  CertificateOfIndigency.objects.all().order_by('id')}
        return render(request, 'IndigencyManagement/indigency_list.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def edit_indigency(request, id):
    if request.user.is_authenticated:
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
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def generate_indigency (request, id):
    if request.user.is_authenticated:
        template_name = "IndigencyManagement/indigency_pdf.html"
        indigency = CertificateOfIndigency.objects.get(pk=id)
        
        return render_to_pdf(
            template_name,
            {
                "indigency": indigency,
            },
        )
    else:
        return redirect('loginPage')
