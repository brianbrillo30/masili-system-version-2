from fileinput import filename
import os
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


def edit_announcement(request, id):
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
    # form = AnnouncementForm(instance=edit)

    # if request.method == 'POST':
    #     form = AnnouncementForm(request.POST,instance=edit)
    #     img = request.POST.get('image')
    #     if form.is_valid():
    #          if img == None:
    #             annupdate = form.save(commit=False)
    #             annupdate.image.name = filename+".jpg"
    #             annupdate.save()

    #             form.save()
    #             return redirect('announcementPage')
    # context = {'form':form, "editA": editA, 'prev_img':editA.image}
    


def delete_announcement(request, id):
    ann = Announcement.objects.get(id=id)

    context = {'ann': ann}
    if request.method == 'POST':
        if len(ann.image) > 0:
            os.remove(ann.image.path)
            ann.delete()
            return redirect('announcementPage')
    return render(request, 'AnnouncementPage/delete_announcement.html', context)
