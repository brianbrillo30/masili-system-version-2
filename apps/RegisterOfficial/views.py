from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from apps.RegisterOfficial.forms import AdminRegistrationForm
from .decorators import superadmin_only
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@superadmin_only
def add_official_account(request):
    if request.user.is_authenticated:
        form = AdminRegistrationForm()
        if request.method == 'POST':
            form = AdminRegistrationForm(request.POST)
            if form.is_valid():
                admin = form.save()
                group = Group.objects.get(name='admin')
                admin.groups.add(group)
                messages.success(request, 'Official account has been registered')
                return redirect('add_official_account')
        else:
            form = AdminRegistrationForm()
        context ={'form': form}
        return render(request, 'RegisterOfficial/register_official.html', context)
    else:
        return redirect('loginPage')
