from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    
    name= models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    address=models.CharField(max_length=100)