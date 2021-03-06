from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import bikeCompanyModel, bikeDisplay, bikeServiceRequestModel, feedBackFormModel
import re

class bikeRegForm(ModelForm):
    # bikeUser = forms.CharField(label="Bike user", widget=forms.TextInput(attrs={
    #     "value" : "user1",
    #     # "hidden": True
    #     "readonly":True
    # }))
    
    def __init__(self, *args, **kwargs):
        self.bikeUser = kwargs.pop('user',None)
        super(bikeRegForm, self).__init__(*args, **kwargs)
        # print("The user = ", self.bikeUser) 

        self.fields['bikeUser'] = forms.CharField(
            widget=forms.TextInput(attrs={
                "value": self.bikeUser,
                "readonly":True
            })
        )
        # self.fields['bikeCompany'].queryset = bikeCompanyModel.objects.all()
        self.fields['bikeCompany'] = forms.ModelChoiceField(queryset= bikeCompanyModel.objects.all(), label="Servicing available only for following company")
    
  
    
    class Meta:
        model = bikeDisplay
        fields = '__all__'


        
class bikeReqUpdate(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     self.serviceUser = kwargs.pop('user', None)
    #     super(bikeReqUpdate, self).__init__(*args, **kwargs)
    #     print("OK = ", self.serviceUser)

    #     self.fields['serviceUser'] = forms.CharField(widget=forms.TextInput(
    #         attrs={
    #             "value": self.serviceUser,
    #             "readonly": True            
    #         }
    #     ))

     

        # onlyDesiredUsersCompanyRecord = bikeDisplay.objects.filter(bikeUser=self.serviceUser).values_list( flat=True)
        # self.fields['serviceCompany'] = forms.ModelChoiceField(
        #      queryset = bikeCompanyModel.objects.filter(id__in = onlyDesiredUsersCompanyRecord).values_list('bikeCompanyNames', flat=True)
        # )

        # onlyDesiredUserBikeRecord = bikeDisplay.objects.filter(bikeUser=self.serviceUser).values_list('bikeModel', flat=True)
        # self.fields['serviceModel'] = forms.ModelChoiceField(
        #     queryset = userBikeModel.objects.filter(id__in = onlyDesiredUserBikeRecord).values_list('bikeModel', flat=True)
        # )     

        # onlyDesiredUserBikeNumber = bikeDisplay.objects.filter(bikeUser=self.serviceUser).values_list('bikeNumber', flat=True)
        # self.fields['serviceNumber'] = forms.ModelChoiceField(
        #     queryset =  onlyDesiredUserBikeNumber
        # )  

        # onlyDesiredUserBikeColor = bikeDisplay.objects.filter(bikeUser=self.serviceUser).values_list('bikeColor', flat=True)
        # self.fields['serviceColor'] = forms.ModelChoiceField(
        #     queryset = onlyDesiredUserBikeColor
        # )    

    
    class Meta:
        model = bikeServiceRequestModel
        fields = [
                    "serviceCompany", "serviceModel",
                    "serviceNumber", "serviceColor", "pickup", "delivery",
                    "kmcovered", "contact", "problem", "deliveryTime"
                 ]

        labels = {
            # "serviceUser": "Rider name",
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



 
class serviceRequestForm(ModelForm):


    # def __init(self, *args, **kwargs):
    #     super(EmployeeSoftwareForm, self).__init__(*args, **kwargs)
    #     if 'instance' in kwargs:
    #     self.fields['assets'].queryset = SoftwareAsset.objects.filter(company = kwargs['instance'].employee.company)

    
    class Meta:
        model = bikeServiceRequestModel
        fields = [
                    "serviceCompany", "serviceModel",
                    "serviceNumber", "serviceColor", "pickup", "delivery",
                    "kmcovered", "contact", "problem", "deliveryTime"
                 ]

        labels = {
            # "serviceUser": "Rider name",
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

        error_messages = {
            'contact':{'invalid':'Incorrect Phone Number'},
            'deliveryTime':{'invalid': 'Incorrect Time'}
        }


class feedBackForm(ModelForm):
    class Meta:
        model = feedBackFormModel
        fields = "__all__"





         

         
        