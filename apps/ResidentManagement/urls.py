from django.urls import path,include
from .views import *




urlpatterns = [
    path('resident/', resident_list, name= 'resident_list'),
    path('Admin Logout/', adminLogout, name='adminLogout'),
    path('ajax/', ajax, name= 'ajax'),
    path('scan/',scan,name='scan'),
    # path('profiles/', profiles, name= 'profiles'),
    path('Resident Details/', details, name= 'details'),

    path('add_profile/',add_profile,name='add_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),


    # path('clear_history/',clear_history,name='clear_history'),
    # path('reset/',reset,name='reset'),


]
