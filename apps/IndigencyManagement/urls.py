from django.urls import path
from .views import *




urlpatterns = [
    path('indigency_request/',indigency_module,name='indigency_request'),
]
