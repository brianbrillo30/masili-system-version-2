from audioop import reverse
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .decorators import admin_only
from .models import *
from .forms import *
import face_recognition
import cv2
import numpy as np
import winsound
from django.db.models import Q
from playsound import playsound
from django.contrib.auth.models import User, Group
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.conf import settings
from django.core.mail import send_mail
from apps.UserPortal.models import clearance as clearance_list, CertificateOfIndigency, BusinessPermit
from apps.ClearanceManagement.forms import*


last_face = 'no_face'
current_path = os.path.dirname(__file__)
sound_folder = os.path.join(current_path, 'sound/')
face_list_file = os.path.join(current_path, 'face_list.txt')
sound = os.path.join(sound_folder, 'beep.wav')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def resident_list(request):
    if request.user.is_authenticated:
        context = {'resident_list' : User.objects.filter(is_superuser=0).order_by('id')}
        return render(request, "ResidentManagement/residents_list.html", context)
    else:
        return redirect('loginPage')

def adminLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Succefull logout')
    return redirect(reverse('loginPage'))

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def ajax(request):
    if request.user.is_authenticated:
        last_face = LastFace.objects.last()
        context = {
            'last_face': last_face
        }
        return render(request, 'ResidentManagement/ajax.html', context)

    else:
        return redirect('loginPage')

@login_required(login_url="loginPage")
@admin_only
def scan(request):

    global last_face

    known_face_encodings = []
    known_face_names = []

    profiles = ResidentsInfo.objects.all()
    for profile in profiles:
        person = profile.image
        image_of_person = face_recognition.load_image_file(f'media/{person}')
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
        known_face_encodings.append(person_face_encoding)
        known_face_names.append(f'{person}'[:-4])


    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:

        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]



                    if last_face != name:
                        
                        # last_face = LastFace(last_face=name)
                        last_face = LastFace.objects.all().last()
                        if last_face == None:
                            last_face = LastFace(last_face=name)
                            last_face.save()
                        else:

                            last_face.last_face = name
                            last_face.save()
                        last_face = name
                        winsound.PlaySound(sound, winsound.SND_ASYNC)
                        
                    else:
                        pass

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)
        cv2.setWindowProperty('Video', cv2.WND_PROP_TOPMOST, 1)
        if cv2.waitKey(1) & 0xFF == 13:
            break
        if (cv2.getWindowProperty('Video', 0) < 0):        
            break 

    video_capture.release()
    cv2.destroyAllWindows()
    return HttpResponse('scaner closed', last_face)

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def details(request):
    if request.user.is_authenticated:
        try:
            last_face = LastFace.objects.last()
            profile = ResidentsInfo.objects.get(Q(image__icontains=last_face))
        except:
            last_face = None
            profile = None

        context = {
            'profile': profile,
            'last_face': last_face,
            'clearance': clearance
        }
        return render(request, 'ResidentManagement/details.html', context)

    else:
        return redirect('loginPage')
   

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def add_profile(request):
    if request.user.is_authenticated:
        form = ProfileForm
        accountForm = UserAccountForm

        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            accountForm = UserAccountForm(request.POST)
            email = request.POST.get('email')

            filename = firstname+" "+lastname

            if form.is_valid() and accountForm.is_valid():

                randomNum = User.objects.make_random_password(length=2, allowed_chars="01234567889")
                random_password = User.objects.make_random_password(length=8, allowed_chars="01234567889")
                username = lastname+randomNum

                user = User.objects.create_user(email = email, username = username, password=random_password)
                group = Group.objects.get(name='resident')
                user.groups.add(group)
                
                subject = 'Welcome to Barangay Masili'
                message = f'Heres your\nUsername: {user.username}\nPassword: {random_password}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail( subject, message, email_from, recipient_list )

                resident = form.save(commit=False)
                resident.image.name = filename+".jpg"
                resident.user = user
                resident.save()

                return redirect('resident_list')

        context={'form':form, 'userform':accountForm}
        return render(request,'ResidentManagement/add_resident.html',context)

    else:
        return redirect('loginPage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def edit_profile(request, id):
    if request.user.is_authenticated:
        profile = ResidentsInfo.objects.get(user=id)
        form = ProfileForm(instance=profile)

        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            img = request.POST.get('image')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            filename = firstname+" "+lastname

            if form.is_valid():
                if img == None:
                    userupdate = form.save(commit=False)
                    userupdate.image.name = filename+".jpg"
                    userupdate.save()
                
                form.save()
                
                return redirect('resident_list')
        context={'form':form, 'prev_img':profile.image}
        return render(request,'ResidentManagement/edit_resident.html',context)
    
    else:
        return redirect('loginPage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def delete_profile(request,id):
    if request.user.is_authenticated:
        profile = User.objects.get(id=id)
        if request.method == 'POST':
            if len(profile.residentsinfo.image) > 0:
                os.remove(profile.residentsinfo.image.path)
                profile.delete()
                return redirect('resident_list')
        return render(request, 'ResidentManagement/delete_resident.html')

    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def view_profile (request, id):
    if request.user.is_authenticated:
        profile = User.objects.get(pk=id)
        context = {'profile': profile}
        return render (request, 'ResidentManagement/view_profile.html', context)

    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def profile_clearance(request, id):
    if request.user.is_authenticated:
        context = {'profile_clearance' : clearance_list.objects.filter(res_id = id)}
        return render(request, 'ResidentManagement/clearance_list.html', context)
        
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def profile_indigency (request, id):
    if request.user.is_authenticated:
        context = {'profile_indigency' : CertificateOfIndigency.objects.filter(res_id = id)}
        return render(request, 'ResidentManagement/indigency_list.html', context)

    else:
        return redirect('loginPage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def profile_business_permit (request, id):
    if request.user.is_authenticated:
        context = {'profile_business_permit' : BusinessPermit.objects.filter(res_id = id)}
        return render(request, 'ResidentManagement/business_permit_list.html', context)
    
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def demographic(request):
    if request.user.is_authenticated:
        cMale = ResidentsInfo.objects.filter(sex_id='1').count
        cFemale = ResidentsInfo.objects.filter(sex_id='2').count

        cMarried = ResidentsInfo.objects.filter(civil_status='1').count
        cSingle = ResidentsInfo.objects.filter(civil_status='2').count
        cDivorced = ResidentsInfo.objects.filter(civil_status='3').count
        cWidowed = ResidentsInfo.objects.filter(civil_status='4').count

        cYes = ResidentsInfo.objects.filter(single_parent='1').count
        # cNo = ResidentsInfo.objects.filter(single_parent='2').count

        # cNone = ResidentsInfo.objects.filter(status='1').count
        cPwd = ResidentsInfo.objects.filter(status='2').count
        cSenior = ResidentsInfo.objects.filter(status='3').count

        cResident = ResidentsInfo.objects.all().count
        

        context = {'cResident': cResident,'cMale': cMale, 'cFemale': cFemale, 'cMarried': cMarried, 'cSingle': cSingle, 
        'cDivorced': cDivorced, 'cWidowed': cWidowed, 'cYes': cYes, 'cPwd': cPwd, 'cSenior': cSenior}
        
        return render(request, 'ResidentManagement/demographic.html', context )
    
    else:
        return redirect('loginPage')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="loginPage")
@admin_only
def adminProfile(request):
    if request.user.is_authenticated:

        return render(request, 'admin_profile.html')
    
    else:
        return redirect('loginPage')




    