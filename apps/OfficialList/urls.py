from django.urls import path
from .views import *


urlpatterns = [
    path('Official List/', officialList ,name='officialList'),
    path('edit_official/<hashid:id>/', edit_official ,name='edit_official'),  
    path('delete_official/<hashid:id>/', delete_official ,name='delete_official'),
]
