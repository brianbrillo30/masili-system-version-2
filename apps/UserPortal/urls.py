from django.urls import path
from django.contrib.auth import views as auth_views


from .views import *
from .forms import CaptchaPasswordChangeForm

urlpatterns = [
    path ('Home/', home, name='home'),
    path ('About/', about, name='about'),
    path ('Contact/', contact, name='contact'),
    path ('Announcement/', announce, name='announce'),
    path ('ServicePortal/', servicesPortal, name='service_portal'),
    path ('Profile/', profile, name='profile'),
    path ('Change Email/', changeEmail, name='changeEmail'),
    path ('Change Username/', changeUsername, name='changeUsername'),
    path ('User Logout/', userLogout, name='userLogout'),
    path ('BarangayClearance/', barangay_clearance, name='barangay_clearance'),
    path ('indigency/', indigency, name='indigency'),
    path ('BuildingPermit/', BuildingPermit, name='BuildingPermit'),
    path ('BusinessPermit/', BusinessPermit, name='BusinessPermit'),
    path ('ResidencyCertificate/', ResidencyCertificate, name='ResidencyCertificate'),
    path ('document-status/', document_status, name='document-status'),



    path('password_change', 
    auth_views.PasswordChangeView.as_view(template_name='ChangePassword/password_change.html', form_class=CaptchaPasswordChangeForm), 
    name='password_change'),

    path('password_change_done', 
    auth_views.PasswordChangeDoneView.as_view(template_name='ChangePassword/password_change_done.html'), 
    name='password_change_done'),
    
]

# urlpatterns = [
#     path ('Home/', index, name='index'),
#     path ('About/', about, name='about'),
#     path('User Logout/', userLogout, name='userLogout'),
#     path ('ServicePortal/', ServicesPortal, name='service_portal'),
#     path ('Login/', userLogin, name='userLogin'),


# ]