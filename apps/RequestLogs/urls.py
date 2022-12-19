from django.urls import path
from .views import *


urlpatterns = [
    path('logs/',requestLogs,name='requestLogs'),
]
