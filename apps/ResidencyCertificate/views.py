from django.shortcuts import render, redirect, HttpResponse
from apps.UserPortal.models import ResidencyCertificate
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
def residency_certificate_module(request):
    if request.user.is_authenticated:
        return render (request, 'ResidencyCertificate/resident_certificate_module.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def residency_certificate_list(request):
    if request.user.is_authenticated:
        context = {'residency_certificate_list':ResidencyCertificate.objects.all().order_by('id')}
        return render(request, 'ResidencyCertificate/residency_certificate_list.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def edit_residency(request, id):
    if request.user.is_authenticated:
        residency_certificate = ResidencyCertificate.objects.get(pk=id)
        form = ResidencyCertificateForm(instance=residency_certificate)

        if request.method == 'POST':
            form = ResidencyCertificateForm(request.POST,instance=residency_certificate)
            if form.is_valid():
                form.save()
                return HttpResponse(status=204, headers={'HX-Trigger': 'ResidencyList'})

        context = {'form':form, 'disabledform':residency_certificate}
        return render(request, 'ResidencyCertificate/residency_certificate_form.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def generate_resident_certificate(request, id):
    if request.user.is_authenticated:
        template_name = "ResidencyCertificate/resident_certificate_pdf.html"
        residency_certificate = ResidencyCertificate.objects.get(pk=id)
        
        return render_to_pdf(
            template_name,
            {
                "residency_certificate": residency_certificate,
            },
        )
    else:
        return redirect('loginPage') 


def delete_resident_certificate_request(request, id):
    if request.user.is_authenticated:
        residency_certificate = ResidencyCertificate.objects.get(pk=id)
        
        context = {'residency_certificate':residency_certificate}
        if request.method == 'POST':

            email_msg = request.POST.get('reason_masage')

            subject = 'Reasons For Denying your Request'
            message = email_msg
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [residency_certificate.res_id.user.email]
            send_mail( subject, message, email_from, recipient_list )

            residency_certificate.delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'ResidencyList'})
        return render(request, 'ResidencyCertificate/delete_resident_certificate.html', context)

    else:
        return redirect('loginPage')
