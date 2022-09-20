from django.urls import path
from .views import *


urlpatterns = [
    path ('Home/', index, name='index'),
    path ('About/', about, name='about'),
    path ('ServicePortal/', ServicesPortal, name='service_portal'),
    path ('Home/Login/', userLogin, name='userLogin'),
    path ('Services/', services, name='services'),

]