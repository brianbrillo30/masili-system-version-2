from django.urls import path
from .views import *


urlpatterns = [
    path('Home/', home, name='home'),
    path ('Login/', userLogin, name='userLogin'),
    path ('ServicePortal/', servicesPortal, name='service_portal'),
    path('User Logout/', userLogout, name='userLogout'),
]

# urlpatterns = [
#     path ('Home/', index, name='index'),
#     path ('About/', about, name='about'),
#     path('User Logout/', userLogout, name='userLogout'),
#     path ('ServicePortal/', ServicesPortal, name='service_portal'),
#     path ('Login/', userLogin, name='userLogin'),


# ]