from django.urls import path
from .views import *




urlpatterns = [
    path ('announcement/', announcementPage, name='announcementPage'),
    path ('add_announcement/', add_announcement, name='add_announcement'),
    path ('announcement_list/', announcement_list, name='announcement_list'),
    path ('edit_announcement/<int:id>/', edit_announcement, name='edit_announcement'),
    path ('delete_announcement/<int:id>/', delete_announcement, name='delete_announcement')
 ]
