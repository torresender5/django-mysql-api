from django.db import models

# Create your models here.

class DoctorModel(models.Model):
    
    # id=models.IntegerField()
    _id= models.CharField(max_length=24)
    name = models.CharField(max_length=50, unique=True)
    lastname = models.CharField(max_length=50)
    identification= models.IntegerField()
    office_address= models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    