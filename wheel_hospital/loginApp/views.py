from django.shortcuts import render, redirect

# IMPORTS FOR LOGIN 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginPageView(request):

    if request.user.is_authenticated:
        return redirect('dash')
    else:    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                messages.info(request, 'Incorrect login credentials')  

        context = {
        }
        return render(request, 'login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


