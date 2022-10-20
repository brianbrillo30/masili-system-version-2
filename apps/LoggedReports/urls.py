from django.urls import path
from .views import *


urlpatterns = [
    path('Logged Reports/', loggedReports ,name='logged_reports'),

]
