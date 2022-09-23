from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(DocumentStatus)
admin.site.register(clearance)
admin.site.register(CertificateOfIndigency)
admin.site.register(BuildingPermit)
admin.site.register(BusinessPermit)
