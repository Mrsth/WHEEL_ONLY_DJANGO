from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class bikeCompanyModel(models.Model):
    bikeCompanyNames = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.bikeCompanyNames

class userBikeModel(models.Model):
    bikeModel = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.bikeModel

class bikeDisplay(models.Model):
    bikeUser = models.CharField(max_length=50)
    # bikeCompany = models.CharField(max_length=50)
    bikeCompany = models.ForeignKey(bikeCompanyModel, on_delete=models.CASCADE)
    # bikeModel = models.CharField(max_length=50)
    bikeModel = models.ForeignKey(userBikeModel, on_delete=models.CASCADE)
    bikeNumber = models.CharField(max_length=50, unique=True)
    bikeColor = models.CharField(max_length=50)
    bikeImage = models.ImageField(upload_to='dbImages')

    def __str__(self) -> str:
        return self.bikeNumber    



class bikeServiceRequestModel(models.Model):

    service_status = (
        ('Completed', 'Completed'),
        ('Not Completed', 'Not Completed'),
        ('On Going', 'On Going'),
    )

    def validate_date(value):
        if value==datetime.now().date():
            pass
        elif value>datetime.now().date():
            raise ValidationError("Don't input future date")  
        elif value<datetime.now().date():
            raise ValidationError('Don\'t input past date') 

    phone_regx =  RegexValidator(r'^[9]\d{9}$', 'Please enter valid phone number')       

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
    kmcovered = models.IntegerField()
    contact = models.CharField(max_length=10, validators=[phone_regx])
    problem = models.TextField()
    completed = models.CharField(max_length=100, default="Not Completed", choices = service_status)
    serviceDate = models.DateField(validators=[validate_date], default=timezone.now) 
    serviceTime = models.TimeField(auto_now=True)
    deliveryTime = models.TimeField()

    def __str__(self) -> str:
        return self.serviceNumber

    
class feedBackFormModel(models.Model):
    userName = models.CharField(max_length=50)
    userFeedBack = models.TextField()
    feedBackTime = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.userName
