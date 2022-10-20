from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from apps.OfficialList.forms import EditAdminProfileForm
# Create your views here.


def officialList(request):
    context = {'admin_list' : User.objects.filter(groups__name__in=['admin']).order_by('id')}
    return render(request, "OfficialList/official_list.html", context)


def delete_official(request,id):
    profile = User.objects.get(id=id)
    context = {'profile': profile}
    if request.method == 'POST':
        profile.delete()
        return redirect('officialList')
    return render(request, 'OfficialList/delete_official.html', context)


def edit_official(request, id):
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
  
   
