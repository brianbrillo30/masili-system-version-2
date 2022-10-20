from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from apps.RegisterOfficial.forms import AdminRegistrationForm
from .decorators import superadmin_only

# Create your views here.
@superadmin_only
def add_official_account(request):
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
