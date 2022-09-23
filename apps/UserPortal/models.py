from django.db import models

from apps.ResidentManagement.models import*
import uuid

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
    transaction_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)


class CertificateOfIndigency(models.Model):
    res_id = models.ForeignKey(ResidentsInfo, on_delete=models.CASCADE, null=True)
    age = models.CharField(max_length=70)
    purpose = models.CharField(max_length=70)
    date_requested = models.DateField(auto_now=True)
    date_released = models.DateField(null=True)
    status = models.ForeignKey(DocumentStatus, on_delete=models.CASCADE, default=1)
    transaction_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

class BuildingPermit(models.Model):
    res_id = models.ForeignKey(ResidentsInfo, on_delete=models.CASCADE, null=True)
    proposed_construction = models.CharField(max_length=255)
    total_area  = models.CharField(max_length=255)
    estimated_cost = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    contractor = models.CharField(max_length=255)
    prepared_by = models.CharField(max_length=255)

    paid_under_or = models.CharField(max_length=255)
    
    date_requested = models.DateField(auto_now=True)
    date_released = models.DateField(null=True)

    amount_paid = models.CharField(max_length=255)
    
    status = models.ForeignKey(DocumentStatus, on_delete=models.CASCADE, default=1)
    transaction_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)


class BusinessPermit(models.Model):
    res_id = models.ForeignKey(ResidentsInfo, on_delete=models.CASCADE, null=True)
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    business_nature = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    residece_certificate_no = models.CharField(max_length=255)
    date_requested = models.DateField(auto_now=True)
    date_released = models.DateField(null=True)
    issued_at = models.CharField(max_length=255)
    capital_investment = models.CharField(max_length=255)
    gross_sales = models.CharField(max_length=255)

    previous_or = models.CharField(max_length=255)
    date_issued = models.DateField(null=True)
    previous_or_issued_at = models.CharField(max_length=255)
    amount_collect = models.CharField(max_length=255)
    paid_or = models.CharField(max_length=255)
    paid_or_date_issued = models.DateField(null=True)
    paid_or_issued_at = models.CharField(max_length=255)
    amount_colledted = models.CharField(max_length=255)
    
    status = models.ForeignKey(DocumentStatus, on_delete=models.CASCADE, default=1)
    transaction_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)




