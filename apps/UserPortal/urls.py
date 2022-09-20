from django.urls import path
from .views import *


urlpatterns = [
    path ('Home/', index, name='index'),
    path ('About/', about, name='about'),
    path ('Home/Login/', userLogin, name='userLogin'),
]