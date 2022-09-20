from django.urls import path
from .views import *


urlpatterns = [
    path ('Home/', index, name='index'),
    path ('About/', about, name='about'),
<<<<<<< HEAD
    path ('ServicePortal/', ServicesPortal, name='service_portal'),
=======
    path ('Home/Login/', userLogin, name='userLogin'),
>>>>>>> db5d86e741def260a7d50c5e769f70868fc79309
]