from django.shortcuts import render, HttpResponse, redirect
from apps.UserPortal.models import clearance as clerance_list
from .forms import *
from project.utils import render_to_pdf
from .decorators import admin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def clearance(request):
    if request.user.is_authenticated:
        return render(request, 'ClearanceManagement/clearance_table.html')
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def clearance_list(request):
    if request.user.is_authenticated:
        context = {'clearance_list' :  clerance_list.objects.all().order_by('id')}
        return render(request, 'ClearanceManagement/clearance_list.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def edit_clearance(request, id):
    if request.user.is_authenticated:

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
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def generate_clearance (request, id):
    if request.user.is_authenticated:
        template_name = "ClearanceManagement/clearance_pdf.html"
        clearance = clerance_list.objects.get(pk=id)
        
        return render_to_pdf(
            template_name,
            {
                "clearance": clearance,
            },
        )
    else:
        return redirect('loginPage')



def delete_clearance(request, id):
    if request.user.is_authenticated:
        clearance = clerance_list.objects.get(pk=id)
        
        context = {'clearance':clearance}
        if request.method == 'POST':
            clearance.delete()
            return HttpResponse(status=204, headers={'HX-Trigger': 'clearancelistUpdate'})
        return render(request, 'ClearanceManagement/delete_clearance.html', context)

    else:
        return redirect('loginPage')


