from django.shortcuts import render, redirect

# IMPORTS FOR REGISTER
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def registerPageView(request):

    if request.user.is_authenticated:
        return redirect('dash')
        

    rForm = CreateUserForm()
    if request.method == 'POST':
        rForm = CreateUserForm(request.POST) # Passing post datas into the userformcreation instance
        if rForm.is_valid():
            rForm.save()
            messages.success(request, 'Account created successfully = ' + rForm.cleaned_data.get('username'))
            # return redirect('login')
            rForm = CreateUserForm()
            return redirect('reg')

    context = {
        'registerForm': rForm
    }
    return render(request, 'register.html', context)

