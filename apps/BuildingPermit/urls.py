from django.urls import path
from .views import *

from project.utils import HashIdConverter
from django.urls import register_converter

register_converter(HashIdConverter, "hashid")



urlpatterns = [
    path('building_permit_request/',building_permit_module,name='building_permit_module'),
    path('building_permit_list/', building_permit_list, name='building_permit_list'),
    path('building_permit_list/<int:id>', edit_building_permit, name='edit_building_permit'),
    path('generate_building_permit/<hashid:id>', generate_building_permit, name='generate_building_permit'),
]
