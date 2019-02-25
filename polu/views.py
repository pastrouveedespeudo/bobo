from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def polution(request):
    return render(request, 'polution.html')
