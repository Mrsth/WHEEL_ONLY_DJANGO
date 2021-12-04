from django.contrib import admin
from django.db import models
from .models import bikeDisplay, bikeServiceRequestModel, bikeCompanyModel, userBikeModel, feedBackFormModel

# Register your models here.
@admin.register(bikeDisplay)
class bikeDisplayAdmin(admin.ModelAdmin):
    list_display = ['bikeUser', 'bikeCompany', 'bikeModel', 'bikeNumber', 'bikeColor', 'bikeImage']

@admin.register(bikeServiceRequestModel)
class bikeRequestFormAdmin(admin.ModelAdmin):
    list_display = ["serviceUser", "serviceCompany", "serviceModel", "serviceNumber", "serviceColor", 
                    "pickup", "delivery", "kmcovered", "contact", "problem", "completed", "serviceDate", "serviceTime", "deliveryTime"]

@admin.register(feedBackFormModel)
class feedBackFormAdmin(admin.ModelAdmin):
    list_display = ["userName", "userFeedBack", "feedBackTime"]


# admin.site.register(bikeDisplay)
# admin.site.register(bikeServiceRequestModel)
admin.site.register(bikeCompanyModel)
admin.site.register(userBikeModel)

admin.site.site_header = "Wheeler's Hospital Admin Panel"
