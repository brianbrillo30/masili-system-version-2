from django.urls import path
from . import views

urlpatterns = [
    path ('Admin Login/', views.adminLogin, name='adminLogin'),
 

]