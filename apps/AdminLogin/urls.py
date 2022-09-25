from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path ('Admin Login/', views.adminLogin, name='adminLogin'),

    path('reset_password_admin/', 
        auth_views.PasswordResetView.as_view(template_name="PasswordResetAdmin/password_reset.html"), 
        name="reset_password_admin"),

    path('reset_password_sent_admin/', 
        auth_views.PasswordResetDoneView.as_view(template_name="PasswordResetAdmin/password_reset_sent.html"), 
        name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="PasswordResetAdmin/password_reset_form.html"), 
        name="password_reset_confirm"),
    
    path('reset_password_complete_admin/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="PasswordResetAdmin/password_reset_done.html"), 
        name="password_reset_complete"),
 

 

]