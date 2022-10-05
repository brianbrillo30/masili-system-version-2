from django.urls import path
from django.contrib.auth import views as auth_views


from .views import *
from .forms import UserPasswordResetForm

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

    
    path('password_change', 
    auth_views.PasswordChangeView.as_view(template_name='ChangePassword/password_change.html'), 
    name='password_change'),

    path('password_change_done', 
    auth_views.PasswordChangeDoneView.as_view(template_name='ChangePassword/password_change_done.html'), 
    name='password_change_done'),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="PasswordReset/password_reset.html", form_class=UserPasswordResetForm), 
        name="reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="PasswordReset/password_reset_sent.html"), 
    name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="PasswordReset/password_reset_form.html"), 
    name="password_reset_confirm"),
    
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="PasswordReset/password_reset_done.html"), 
    name="password_reset_complete"),
]

# urlpatterns = [
#     path ('Home/', index, name='index'),
#     path ('About/', about, name='about'),
#     path('User Logout/', userLogout, name='userLogout'),
#     path ('ServicePortal/', ServicesPortal, name='service_portal'),
#     path ('Login/', userLogin, name='userLogin'),


# ]