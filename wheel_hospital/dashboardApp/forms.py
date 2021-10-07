from django.db import models
from django.forms import ModelForm
from .models import bikeDisplay, bikeServiceRequestModel

class bikeRegForm(ModelForm):
    class Meta:
        model = bikeDisplay
        fields = '__all__'

class bikeReqUpdate(ModelForm):
    class Meta:
        model = bikeServiceRequestModel
        fields = [
                    "serviceUser", "serviceCompany", "serviceModel",
                    "serviceNumber", "serviceColor", "pickup", "delivery",
                    "kmcovered", "contact", "problem", "serviceDate", "serviceTime",
                    "deliveryTime"
                 ]