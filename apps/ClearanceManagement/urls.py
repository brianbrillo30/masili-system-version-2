from django.urls import path,include
from .views import *




urlpatterns = [
    path('clearance/',clearance,name='clearance'),
    path('clearance/edit_clearance/<int:id>', edit_clearance, name='edit_clearance' ),
    path('clearance_list', clearance_list, name='clearance_list'),
    path('generate_clearance/<int:id>', generate_clearance, name='generate_clearance'),
]
