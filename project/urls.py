from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Masili/',include('apps.Dashboard.urls')),
    path('Masili/',include('apps.AdminProfile.urls')),
    path('Masili/',include('apps.ResidentManagement.urls')),
    path('Masili/',include('apps.ClearanceManagement.urls')),
    path('Masili/',include('apps.IndigencyManagement.urls')),
    path('Masili/',include('apps.BusinessPermit.urls')),
    path('Masili/',include('apps.BuildingPermit.urls')),
    path('Masili/',include('apps.ResidencyCertificate.urls')),

    path('Barangay Masili/',include('apps.Login.urls')),
    path('Barangay Masili/',include('apps.UserPortal.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
