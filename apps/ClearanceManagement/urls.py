from django.urls import path,include
from .views import *
from project.utils import HashIdConverter
from django.urls import register_converter

register_converter(HashIdConverter, "hashid")



urlpatterns = [
    path('clearance/',clearance,name='clearance'),
    path('clearance/edit_clearance/<int:id>', edit_clearance, name='edit_clearance' ),
    path('clearance_list', clearance_list, name='clearance_list'),
    path('generate_clearance/<hashid:id>', generate_clearance, name='generate_clearance'),
]
