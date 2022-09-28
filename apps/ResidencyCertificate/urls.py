from django.urls import path
from .views import *




urlpatterns = [
    path('residency_request/',residency_certificate_module,name='residency_certificate_module'),
    path('residency/',residency_certificate_list,name='residency_certificate_list'),
    path('residency/<int:id>', edit_residency, name='edit_residency'),
    path('generate_resident_certificate/<int:id>', generate_resident_certificate, name='generate_resident_certificate'),
    
]