from django.urls import path
from .views import *
from project.utils import HashIdConverter
from django.urls import register_converter

register_converter(HashIdConverter, "hashid")



urlpatterns = [
    path('indigency_request/',indigency_module,name='indigency_request'),
    path('indigency/', indigency_list, name='indigency_list'),
    path('indigency/<int:id>', edit_indigency, name='edit_indigency'),
    path('generate_indigency/<hashid:id>', generate_indigency, name='generate_indigency'),
]
