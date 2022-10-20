from django.urls import path,include
from .views import *

from project.utils import HashIdConverter
from django.urls import register_converter

register_converter(HashIdConverter, "hashid")

urlpatterns = [
    path('resident/', resident_list, name= 'resident_list'),
    path('admin-logout/', adminLogout, name='adminLogout'),
    path('ajax/', ajax, name= 'ajax'),
    path('scan/', scan,name='scan'),
 
    path('Resident Details/', details, name= 'details'),
    path('PWD/', pwd, name= 'pwd'),
    path('Senior Citizen/', senior, name= 'senior'),
    path('Single Parent/', single, name= 'single'),

    path('add_profile/',add_profile,name='add_profile'),
    path('view_profile/<hashid:id>/',view_profile, name='view_profile'),
    path('edit_profile/<hashid:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<hashid:id>/',delete_profile,name='delete_profile'),
    path('print_data/<hashid:id>/', print_data, name='print_data'),

    # Resident document
    path('clearance/<int:id>/', profile_clearance, name ='profile_clearance'),
    path('indigency/<int:id>/', profile_indigency, name ='profile_indigency'),
    path('business-permit/<int:id>/', profile_business_permit, name ='profile_business_permit'),
    path('building-permit/<int:id>/', profile_building_permit, name='profile_building_permit'),
    path('residency-certificate/<int:id>/', profile_residency_certificate, name='profile_residency_certificate'),
    

    # path('clear_history/',clear_history,name='clear_history'),
    # path('reset/',reset,name='reset'),


]
