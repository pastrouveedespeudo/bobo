from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def polution(request):
    return render(request, 'polution.html')

def charger(request):
    return render(request, 'charger.html')

def polution_lyon(request):
    return render(request, 'polution_lyon.html')

def polution_marseille(request):
    return render(request, 'polution_marseille.html')

def polution_paris(request):
    return render(request, 'polution_paris.html')
