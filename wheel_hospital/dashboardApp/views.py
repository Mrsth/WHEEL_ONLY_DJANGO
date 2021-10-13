from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# IMPORTS FOR DASHBOARD
from django.contrib.auth.decorators import login_required
from .models import bikeCompanyModel, bikeDisplay, bikeServiceRequestModel, userBikeModel
from .forms import bikeRegForm, bikeReqUpdate, serviceRequestForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
@login_required(login_url='login')
def dashboardView(request):
    bikes = bikeDisplay.objects.filter(bikeUser=request.user)
    buttonShowOrNot = list(bikeServiceRequestModel.objects.filter(serviceUser=request.user).values_list('serviceNumber', flat=True))
    
    context = {
        'bikes': bikes,
        'flag': buttonShowOrNot
    }
    return render(request, 'dashboard.html',context)

@login_required(login_url='login')
def bikeRegisterForm(request):
    fm = bikeRegForm(user=request.user)

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
    stat = bikeServiceRequestModel.objects.filter(serviceUser=request.user)
    forCountingRegisteredBikes = bikeDisplay.objects.filter(bikeUser=request.user)

    # bikeNum = [i.serviceNumber for i in stat]
    # print("ONLY BIKE NUMBER = ", bikeNum)

    num_img = []

    for i in stat:
        number = list(bikeDisplay.objects.filter(bikeNumber=i.serviceNumber).values_list('bikeNumber', flat=True))
        img = list(bikeDisplay.objects.filter(bikeNumber=i.serviceNumber).values_list('bikeImage', flat=True))
        print("NUMBER RELATED IMAGES = ", num_img.append((number[0],"/media/"+img[0])))
        
      
    


    context={
        'stat':stat,
        'count': len(forCountingRegisteredBikes),
        'num_img': num_img
    }
    return render(request, 'status.html', context)



@login_required(login_url='login')
def requestDelete(request, pk):
    delRequest = bikeServiceRequestModel.objects.filter(id=pk)
    delRequest.delete()

    # stat = bikeServiceRequestModel.objects.filter(serviceUser=request.user)
    # context={
    #     'stat':stat
    # }

    # return render(request, 'status.html', context)

    return redirect('/status/{{request.user}}')

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


@login_required(login_url='login')
def give_it_to_service(request,pk):
    onlySelectedBikeRecord = bikeDisplay.objects.get(id=pk)

    values = bikeDisplay.objects.filter(id=pk)
    print("values = ", values[0].bikeUser)

    initial = {
                "serviceUser": request.user,
                "serviceCompany": values[0].bikeCompany,
                "serviceModel":values[0].bikeModel,
                "serviceNumber":values[0].bikeNumber,
                "serviceColor": values[0].bikeColor
            }
    fm = serviceRequestForm(initial = initial)

       

    if request.method == 'POST':
        fm = serviceRequestForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            fm = serviceRequestForm()
            return redirect('/status/{{request.user}}')
        else:
            return HttpResponse("Not valid form")        


    context={
        "fm":fm, 
        "onlySelectedBikeRecord":onlySelectedBikeRecord
    }


    return render(request, 'newReqForm.html', context)

    