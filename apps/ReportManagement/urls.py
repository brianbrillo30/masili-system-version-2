from django.urls import path
from .views import *

urlpatterns = [
    path('reports/',reports,name='reports'),
    path('clerancereport/', clearance_reports, name='clearance_reports'),
    path('indigencyreports/', indigency_reports, name='indigency_reports'),
    path('businessreports/', business_reports, name='business_reports'),
    path('buildingreports/', building_reports, name='building_reports'),
    path('residencyreports/', residency_reports, name='residency_reports'),
]
