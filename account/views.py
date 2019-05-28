"""This is view for login, register and logout from accounts app"""

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import UserLoginForm, UserRegisterForm
from .models import Accounts


def my_account(request):
    """this is access to personel account"""
    return render(request, "mon_compte.html", {})


def login_view(request):
    """Here we define the login view"""

    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,
                            password=password)
        
        login(request, user)
        
        if next:
            return redirect(next)
        
        return redirect('/')

    context = {'form':form}

    return render(request, 'login.html', context)


def register_view(request):
    """Here we define the register view"""

    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():

        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        
        acc = Accounts(name=user.username)
        acc.save()
        
        new_user = authenticate(username=user.username,
                                password=password)

        login(request, new_user)

        if next:
            return redirect(next)
        return redirect('/')

    context = {'form':form}

    return render(request, 'signup.html', context)


def logout_view(request):
    """Here we define logout session"""

    logout(request)
    print("déconnexion")
    return redirect('/')
