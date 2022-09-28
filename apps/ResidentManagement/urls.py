from django.urls import path,include
from .views import *




urlpatterns = [
    path('resident/', resident_list, name= 'resident_list'),
    path('Admin Logout/', adminLogout, name='adminLogout'),
    path('ajax/', ajax, name= 'ajax'),
    path('scan/',scan,name='scan'),
    path('Admin Profile/', adminProfile, name= 'adminProfile'),
    path('Resident Details/', details, name= 'details'),

    path('add_profile/',add_profile,name='add_profile'),
    path('view_profile/<int:id>/',view_profile, name='view_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),

    # Resident document
    path('clearance/<int:id>/', profile_clearance, name ='profile_clearance'),
    path('indigency/<int:id>/', profile_indigency, name ='profile_indigency'),
    path('business_permit/<int:id>/', profile_business_permit, name ='profile_business_permit'),
    path('building_permit/<int:id>/', profile_building_permit, name='profile_building_permit'),

    path('Demographic/', demographic, name='demographic'),
    # path('clear_history/',clear_history,name='clear_history'),
    # path('reset/',reset,name='reset'),


]
