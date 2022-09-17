from django.urls import path
from .views import *


urlpatterns = [
    path ('Home', index, name='index')
]