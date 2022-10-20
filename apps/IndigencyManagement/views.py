from django.shortcuts import render, redirect, HttpResponse
from apps.UserPortal.models import CertificateOfIndigency
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

def delete_indigency(request, id):
    if request.user.is_authenticated:
        indigency = CertificateOfIndigency.objects.get(pk=id)
        
        context = {'indigency':indigency}
        if request.method == 'POST':

            email_msg = request.POST.get('reason_masage')

            subject = 'Reasons For Denying your Request'
            message = email_msg
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [indigency.res_id.user.email]
            send_mail( subject, message, email_from, recipient_list )

            indigency.delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'indigencylistUpdate'})
        return render(request, 'IndigencyManagement/delete_indigency.html', context)

    else:
        return redirect('loginPage')
