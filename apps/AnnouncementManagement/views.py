from django.shortcuts import render,redirect, HttpResponse

from apps.AnnouncementManagement.forms import AnnouncementForm
from .models import Announcement
from django.contrib.auth.decorators import login_required
from .decorators import admin_only

# Create your views here.

@login_required(login_url="loginPage")
@admin_only
def announcementPage(request):
    return render (request, 'AnnouncementPage/announcement.html')


@login_required(login_url="loginPage")
@admin_only
def announcement_list(request):
    context = {'announcementList' :  Announcement.objects.all()}
    return render(request, 'AnnouncementPage/announcement_list.html', context)

@login_required(login_url="loginPage")
@admin_only
def add_announcement(request):
    form = AnnouncementForm
    if request.method == 'POST':
        form = AnnouncementForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'announcementAdd'})
    return render (request, 'AnnouncementPage/announcement_form.html', {'form': form})
