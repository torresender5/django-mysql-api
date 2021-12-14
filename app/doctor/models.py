from django.db import models

# Create your models here.

class DoctorModel(models.Model):
    
    # id=models.IntegerField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    office_address= models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    