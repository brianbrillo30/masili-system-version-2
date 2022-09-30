from django.urls import path
from .views import *




urlpatterns = [
    path ('announcement/', announcement, name='announcement'),
    path ('add_announcement/', add_announcement, name='add_announcement'),
]
