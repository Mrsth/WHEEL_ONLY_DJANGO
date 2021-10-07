from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class bikeDisplay(models.Model):
    bikeUser = models.CharField(max_length=50)
    bikeCompany = models.CharField(max_length=50)
    bikeModel = models.CharField(max_length=50)
    bikeNumber = models.CharField(max_length=50)
    bikeColor = models.CharField(max_length=50)
    bikeImage = models.ImageField(upload_to='dbImages')

class bikeCompanyModel(models.Model):
    bikeCompanyNames = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.bikeCompanyNames

class userBikeModel(models.Model):
    bikeModel = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.bikeModel

class bikeServiceRequestModel(models.Model):

    def validate_date(value):
        if value==datetime.now().date():
            pass
        elif value>datetime.now().date():
            raise ValidationError("Don't input future date")  
        elif value<datetime.now().date():
            raise ValidationError('Don\'t input past date') 

    # serviceUser = models.CharField(max_length=50)
    # serviceCompany = models.CharField(max_length=50)
    # serviceModel = models.CharField(max_length=50)
    serviceUser = models.ForeignKey(User, on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(bikeCompanyModel, on_delete=models.CASCADE)
    serviceModel = models.ForeignKey(userBikeModel, on_delete=models.CASCADE)
    serviceNumber = models.CharField(max_length=50, unique=True)
    serviceColor = models.CharField(max_length=50)

    pickup = models.CharField(max_length=50)
    delivery = models.CharField(max_length=50)
    kmcovered = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    problem = models.TextField()
    completed = models.CharField(max_length=100, default="Not Completed")
    serviceDate = models.DateField(validators=[validate_date], default=timezone.now) 
    serviceTime = models.TimeField(auto_now=True)
    deliveryTime = models.TimeField()

    def __str__(self) -> str:
        return self.serviceNumber

    

