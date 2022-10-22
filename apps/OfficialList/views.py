from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from apps.OfficialList.forms import EditAdminProfileForm
from .decorators import superadmin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@superadmin_only
def officialList(request):
    if request.user.is_authenticated:
        context = {'admin_list' : User.objects.filter(groups__name__in=['admin']).order_by('id')}
        return render(request, "OfficialList/official_list.html", context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@superadmin_only
def delete_official(request,id):
    if request.user.is_authenticated:
        profile = User.objects.get(id=id)
        context = {'profile': profile}
        if request.method == 'POST':
            profile.delete()
            return redirect('officialList')
        return render(request, 'OfficialList/delete_official.html', context)
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@superadmin_only
def edit_official(request, id):
    if request.user.is_authenticated:
        profile = User.objects.get(id=id)
        form = EditAdminProfileForm(instance=profile)
        if request.method == 'POST':
            form = EditAdminProfileForm(request.POST, instance=profile)

            if form.is_valid():
                form.save()
                return redirect('officialList')
        else:
            form = EditAdminProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'OfficialList/edit_official.html', context)
    else:
        return redirect('loginPage')
    
   
