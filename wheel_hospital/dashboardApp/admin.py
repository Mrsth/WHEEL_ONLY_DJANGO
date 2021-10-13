from django.contrib import admin
from django.db import models
from .models import bikeDisplay, bikeServiceRequestModel, bikeCompanyModel, userBikeModel

# Register your models here.
@admin.register(bikeDisplay)
class bikeDisplayAdmin(admin.ModelAdmin):
    list_display = ['bikeUser', 'bikeCompany', 'bikeModel', 'bikeNumber', 'bikeColor', 'bikeImage']



# admin.site.register(bikeDisplay)
admin.site.register(bikeServiceRequestModel)
admin.site.register(bikeCompanyModel)
admin.site.register(userBikeModel)
