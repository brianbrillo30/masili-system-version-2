from django.db import models

from apps.ResidentManagement.models import*

# Create your models here.


class DocumentStatus(models.Model):
    document_status = models.CharField(max_length=70)

    def __str__(self):
        return self.document_status    
    

class clearance(models.Model):
    res_id = models.ForeignKey(ResidentsInfo, on_delete=models.CASCADE, null=True)
    age = models.CharField(max_length=70)
    purpose = models.CharField(max_length=70)
    date_requested = models.DateField(auto_now=True)
    date_released = models.DateField(null=True)
    status = models.ForeignKey(DocumentStatus, on_delete=models.CASCADE, default=1)



