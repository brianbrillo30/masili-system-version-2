from django.urls import path,include
from .views import *


urlpatterns = [
    path('Admin Profile/', adminProfile, name='adminProfile'),
]