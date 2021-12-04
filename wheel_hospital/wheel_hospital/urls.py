"""wheel_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from loginApp.views import loginPageView, logoutView
from registerApp.views import registerPageView
from dashboardApp.views import (dashboardView, bikeRegisterForm, updateBikeInfo, deleteBikeInfo, bikeStatus,
                                 requestDelete, requestUpdate, passwordReset, give_it_to_service, aboutUsView, error_page)
from blogApp.views import blogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginPageView, name="login"),
    path('reg/', registerPageView, name="reg"),
    path('dash/', dashboardView, name="dash"),
    path('logout/', logoutView, name="logout"),
    path('bikeReg/', bikeRegisterForm, name="bikeReg"),
    path('blog/', blogView, name="blog"),
    path('dash/update/<str:pk>', updateBikeInfo, name="updateBike"),
    path('dash/del/<str:pk>', deleteBikeInfo, name="deleteBike"),
    path('status/<str:name>', bikeStatus, name='status'),
    path('status/delete/<str:pk>', requestDelete, name='delete'),
    path('update/<str:pk>', requestUpdate, name='update'),
    path('reset/<str:name>', passwordReset, name='reset'),
    path('service/<str:pk>', give_it_to_service, name='service'),
    path('about/', aboutUsView, name='about'),
    path('error/', error_page, name="error")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
