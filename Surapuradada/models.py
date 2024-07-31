from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    
class Managers(models.Model): 
  managerId = models.CharField(max_length=25, primary_key=True)
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=18)
  brandName = models.CharField(max_length=50)
  contactNum = models.IntegerField()
  activeStatus = models.BooleanField(default=False)
  activeDays = models.IntegerField(default=0)

class Brands(models.Model):
  brandId = models.CharField(max_length=12, primary_key=True)
  managerId = models.ForeignKey(Managers, on_delete=models.CASCADE)
  brandName = models.CharField(max_length=50)
  storeCount = models.IntegerField()
  price = models.IntegerField()
  startDate = models.DateField()
  embedLink = models.CharField(max_length=120)
  imagePath = models.ImageField(upload_to='logos/')

class Stores(models.Model): 
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  storeId = models.CharField(max_length=12, primary_key=True)
  brandId = models.ForeignKey(Brands, on_delete=models.CASCADE)
  managerId = models.ForeignKey(Managers, on_delete=models.CASCADE)
  email = models.EmailField()
  password = models.CharField(max_length=18)
  storeName = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  activeStatus = models.BooleanField()
  activeDays = models.IntegerField()
  contactNum = models.IntegerField()
  storeCode = models.CharField(max_length=255, null=True)

class Logs(models.Model):
  logId = models.CharField(max_length=15, primary_key=True)
  user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
  type = models.BooleanField()
  ipadd = models.GenericIPAddressField()
  stamp = models.TimeField()
  browser = models.CharField(max_length=45)
  date = models.DateField()



