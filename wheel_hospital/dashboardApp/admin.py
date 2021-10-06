from django.contrib import admin
from .models import bikeDisplay, bikeServiceRequestModel, bikeCompanyModel, userBikeModel

# Register your models here.
admin.site.register(bikeDisplay)
admin.site.register(bikeServiceRequestModel)
admin.site.register(bikeCompanyModel)
admin.site.register(userBikeModel)
