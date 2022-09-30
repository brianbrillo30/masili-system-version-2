from django.shortcuts import render

# Create your views here.

def announcement(request):
    return render (request, 'AnnouncementPage/announcement.html')

def add_announcement(request):
    return render (request, 'AnnouncementPage/announcement_form.html')
