from fileinput import filename
import os
from django.shortcuts import render,redirect, HttpResponse
from apps.AnnouncementManagement.forms import AnnouncementForm
from .models import Announcement
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def announcementPage(request):
    if request.user.is_authenticated:
        return render (request, 'AnnouncementPage/announcement.html')
    else:
        return redirect('loginPage')


@login_required(login_url="loginPage")
@admin_only
def announcement_list(request):
    if request.user.is_authenticated:
        context = {'announcementList' :  Announcement.objects.all()}
        return render(request, 'AnnouncementPage/announcement_list.html', context)
    else:
        return redirect('loginPage')

@login_required(login_url="loginPage")
@admin_only
def add_announcement(request):
    if request.user.is_authenticated:
        form = AnnouncementForm
        if request.method == 'POST':
            form = AnnouncementForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse(status=204, headers={'HX-Trigger': 'announcementAdd'})
        return render (request, 'AnnouncementPage/announcement_form.html', {'form': form})
    else:
        return redirect('loginPage')

@login_required(login_url="loginPage")
@admin_only
def edit_announcement(request, id):
    if request.user.is_authenticated:
        edit = Announcement.objects.get(id=id)

        if request.method == "POST":
            if len(request.FILES) != 0:
                if len(edit.image.path) > 0:
                    os.remove(edit.image.path)
                edit.image = request.FILES['image']
            edit.title = request.POST.get('title')
            edit.body = request.POST.get('body')
            edit.save()
            return redirect('announcementPage')
                
        context = {'edit': edit}
        return render(request, 'AnnouncementPage/edit_announcement.html',context)
    else:
        return redirect('loginPage')

@login_required(login_url="loginPage")
@admin_only
def delete_announcement(request, id):
    if request.user.is_authenticated:
        ann = Announcement.objects.get(id=id)

        context = {'ann': ann}
        if request.method == 'POST':
            if len(ann.image) > 0:
                os.remove(ann.image.path)
                ann.delete()
                return redirect('announcementPage')
        return render(request, 'AnnouncementPage/delete_announcement.html', context)
    else:
        return redirect('loginPage')
