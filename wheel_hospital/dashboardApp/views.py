from django.shortcuts import render, redirect

# IMPORTS FOR DASHBOARD
from django.contrib.auth.decorators import login_required
from .models import bikeDisplay, bikeServiceRequestModel
from .forms import bikeRegForm, bikeReqUpdate
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
@login_required(login_url='login')
def dashboardView(request):
    bikes = bikeDisplay.objects.filter(bikeUser=request.user)
    context = {
        'bikes': bikes
    }
    return render(request, 'dashboard.html',context)

@login_required(login_url='login')
def bikeRegisterForm(request):
    fm = bikeRegForm()
    print("ok = ", request.POST, request.method)

    if request.method == "POST":
        fm = bikeRegForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('dash')

    context = {
        "fm" : fm
    }

    

    return render(request, 'bikeRegistration.html', context)

@login_required(login_url='login')
def updateBikeInfo(request, pk):
   info = bikeDisplay.objects.get(id=pk)
   filledForm = bikeRegForm(instance=info)
   
   if request.method == 'POST':
        # filledForm = bikeRegForm(request.POST, instance=info)
        filledForm = bikeRegForm(request.POST, request.FILES, instance=info)
        # print("OKOKOK = ", request.POST)
        if filledForm.is_valid():
            filledForm.save()
            return redirect('dash')
        else:
            return render(request, 'errorPage.html',{})   

   context = {'info': info, 'filledForm': filledForm}
   return render(request, 'bikeUpdateForm.html', context)


@login_required(login_url='login')
def deleteBikeInfo(request, pk):
    delObject = bikeDisplay.objects.get(id=pk)
    delObject.delete()
    return redirect('dash')

@login_required(login_url='login')
def bikeStatus(request, name):
    normalServiceRequestForm = bikeReqUpdate()
    stat = bikeServiceRequestModel.objects.filter(serviceUser=request.user)
    forCountingRegisteredBikes = bikeDisplay.objects.filter(bikeUser=request.user)
    print("Count = ", len(forCountingRegisteredBikes))

    if request.method == "POST":
        normalServiceRequestForm = bikeReqUpdate(request.POST)
        if normalServiceRequestForm.is_valid():
            normalServiceRequestForm.save()
            normalServiceRequestForm = bikeReqUpdate()
        # else:
        #      return render(request, 'errorPage.html',{})   

    context={
        'stat':stat,
        'normalServiceRequestForm':normalServiceRequestForm,
        'count': len(forCountingRegisteredBikes)
    }
    return render(request, 'status.html', context)



@login_required(login_url='login')
def requestDelete(request, pk):
    delRequest = bikeServiceRequestModel.objects.filter(id=pk)
    delRequest.delete()

    stat = bikeServiceRequestModel.objects.filter(serviceUser=request.user)
    context={
        'stat':stat
    }

    return render(request, 'status.html', context)

# import pdb
@login_required(login_url='login')
def requestUpdate(request, pk):
    # pdb.set_trace() 
    updateReqModel = bikeServiceRequestModel.objects.get(id=pk)
    reqFilledForm = bikeReqUpdate(instance=updateReqModel)


    if request.method == 'POST':
        reqFilledForm = bikeReqUpdate(request.POST, request.FILES, instance=updateReqModel)
        print("REQUEST.POST = ", request.POST)
        if reqFilledForm.is_valid():
            reqFilledForm.save()
            return redirect('/status/{pk}')
        else:
            return render(request, 'errorPage.html')

    context = {
            'reqFilledForm': reqFilledForm,
            'pk': pk
    } 

    return render(request, 'serviceReqUpdate.html', context)


@login_required(login_url='login')
def passwordReset(request, name):

    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('dash')
    else:
        fm = PasswordChangeForm(user=request.user)     

    return render(request, 'passwordReset.html', {"fm":fm})

    