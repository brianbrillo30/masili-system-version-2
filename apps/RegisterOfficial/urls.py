from django.urls import path
from .views import *


urlpatterns = [
    path('registerofficial/',add_official_account,name='add_official_account'),
]
