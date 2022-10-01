from django.shortcuts import render,redirect, HttpResponse

from apps.AnnouncementManagement.forms import AnnouncementForm


# Create your views here.

def announcement(request):
    return render (request, 'AnnouncementPage/announcement.html')

def add_announcement(request):
    form = AnnouncementForm
    if request.method == 'POST':
        form = AnnouncementForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'addAnnouncement'})
    return render (request, 'AnnouncementPage/announcement_form.html', {'form': form})
