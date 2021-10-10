from django import forms
from django.db import models
from django.forms import ModelForm, widgets
from django.http import request
from .models import bikeDisplay, bikeServiceRequestModel
from django.contrib.auth.models import User

class bikeRegForm(ModelForm):
    bikeUser = forms.CharField(label="Bike user", widget=forms.TextInput(attrs={
        "value" : "user1",
        # "hidden": True
        "readonly":True
    }))

    class Meta:
        model = bikeDisplay
        fields = '__all__'
        
        
class bikeReqUpdate(ModelForm):
    
    class Meta:
        model = bikeServiceRequestModel
        fields = [
                    "serviceUser", "serviceCompany", "serviceModel",
                    "serviceNumber", "serviceColor", "pickup", "delivery",
                    "kmcovered", "contact", "problem", "deliveryTime"
                 ]

        labels = {
            "serviceUser": "Rider name",
            "serviceCompany": "Rider's bike company",
            "serviceModel": "Rider's bike model",
            "serviceColor": "Bike color",
            "pickup": "Bike pickup location",
            "delivery": "Bike delivary location",
            "kmcovered": "Distance covered (Km)",
            "contact": "Rider's contact number",
            "problem": "Problems",
            "deliveryTime": "Customer's expected delivery time"
        }   

 

         
        