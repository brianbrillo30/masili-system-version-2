from django.shortcuts import render, redirect
from apps.ResidentManagement.models import ResidentsInfo
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .decorators import admin_only
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def dashboard(request):
    if request.user.is_authenticated:
        cMale = ResidentsInfo.objects.filter(sex_id='1').count
        cFemale = ResidentsInfo.objects.filter(sex_id='2').count

        cSingle = ResidentsInfo.objects.filter(civil_status='1').count
        cMarried = ResidentsInfo.objects.filter(civil_status='2').count
        cDivorced = ResidentsInfo.objects.filter(civil_status='3').count
        cWidowed = ResidentsInfo.objects.filter(civil_status='4').count

        cYes = ResidentsInfo.objects.filter(single_parent='1').count
   
        cPwd = ResidentsInfo.objects.filter(status='2').count
        cSenior = ResidentsInfo.objects.filter(status='1').count

        cResident = ResidentsInfo.objects.all().count
                
        context = {'cResident': cResident,'cMale': cMale, 'cFemale': cFemale, 'cMarried': cMarried, 'cSingle': cSingle, 
        'cDivorced': cDivorced, 'cWidowed': cWidowed, 'cYes': cYes, 'cPwd': cPwd, 'cSenior': cSenior}
                
        return render(request, 'Dashboard/demographic.html', context )

    else:
        return redirect('loginPage')

