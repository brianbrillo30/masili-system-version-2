import datetime
from time import time
import random
from django.db import models
from django.contrib.auth.models import User

def random_string():
    return str(random.randint(10000, 99999))

class Purok(models.Model): 
    purok_no = models.CharField(max_length=50)

    def __str__(self):
        return self.purok_no

class Sex(models.Model): 
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.sex

class EducAttainment(models.Model): 
    educ_attainment = models.CharField(max_length=50)

    def __str__(self):
        return self.educ_attainment

class CivilStatus(models.Model): 
    civil_status = models.CharField(max_length=50)

    def __str__(self):
        return self.civil_status

class Status(models.Model): 
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status
    
class ResidentsInfo(models.Model):
    res_id = models.CharField(default= random_string, unique=True, max_length=5)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)

    firstname = models.CharField(max_length=70)
    middlename = models.CharField (max_length=70)
    lastname = models.CharField(max_length=70)
    suffix = models.CharField (max_length=70)
    sex = models.ForeignKey (Sex, on_delete=models.CASCADE)

    phone = models.CharField (max_length=70)

    birthdate = models.DateField ()
    birthplace = models.CharField (max_length=255)
    civil_status = models.ForeignKey (CivilStatus, on_delete=models.CASCADE)
    citizenship = models.CharField (max_length=255)
    purok = models.ForeignKey (Purok, on_delete=models.CASCADE)
    address = models.CharField (max_length=255)
    occupation = models.CharField (max_length=255)
    educ_attainment = models.ForeignKey (EducAttainment, on_delete=models.CASCADE)
    single_parent = models.CharField (max_length=10)
    status = models.ForeignKey (Status, on_delete=models.CASCADE)

    years_resided = models.CharField(max_length=70, null=True)
    
    image = models.ImageField(upload_to='residents-profile')
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.firstname +' '+self.middlename+' '+self.lastname

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = ResidentsInfo.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(ResidentsInfo, self).save(*args, **kwargs)
        

class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face


class DetectedFace(models.Model):
    detected_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.detected_face



