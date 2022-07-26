from datetime import datetime
from distutils.command.upload import upload
import email
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class uppic(models.Model):
    username=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='imgs',blank=True)
    desc=models.TextField(max_length=200)
    timedate=models.DateTimeField(auto_now_add=True, null=True)

class cont(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mob=models.CharField(max_length=20)
    message=models.TextField(max_length=200)
