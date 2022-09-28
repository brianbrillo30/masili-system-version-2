from django.urls import path
from .views import *




urlpatterns = [
    path('business_permit_request/',building_permit_module,name='building_permit_module'),
    path('business_permit_list/',business_permit_list,name='business_permit_list'),
    path('businessPermit/<int:id>', edit_business_permit, name='edit_business_permit'),
    path('generate_business_permit/<int:id>', generate_business_permit, name='generate_business_permit'),
]
