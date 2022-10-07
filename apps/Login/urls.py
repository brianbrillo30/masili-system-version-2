from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .forms import CaptchaPasswordResetForm, UserPasswordResetForm

urlpatterns = [
    path ('Login/', views.loginPage, name='loginPage'),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="PasswordReset/password_reset.html", form_class=UserPasswordResetForm), 
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="PasswordReset/password_reset_sent.html"), 
        name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="PasswordReset/password_reset_form.html", form_class=CaptchaPasswordResetForm), 
        name="password_reset_confirm"),
    
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="PasswordReset/password_reset_done.html"), 
        name="password_reset_complete"),
 

 

]