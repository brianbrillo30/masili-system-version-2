from django.urls import path
from .views import *




urlpatterns = [
    path('indigency_request/',indigency_module,name='indigency_request'),
    path('indigency/', indigency_list, name='indigency_list'),
    path('indigency/<int:id>', edit_indigency, name='edit_indigency'),
    path('generate_indigency/<int:id>', generate_indigency, name='generate_indigency'),
]
