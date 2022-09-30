from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Admin Profile/', adminProfile, name='adminProfile'),

    path('password_change', 
    auth_views.PasswordChangeView.as_view(template_name='ChangePassword/password_change.html'), 
    name='password_change'),

    path('password_change_done', 
    auth_views.PasswordChangeDoneView.as_view(template_name='ChangePassword/password_change_done.html'), 
    name='password_change_done'),
]