from django.shortcuts import render

def mode(request):
    return render(request, "mode.html")


def database_mode(request):
    return render(request, "database_mode.html")


def tendance(request):
    return render(request, "tendance.html")

def ajout(request):
    return render(request, "ajout.html")

def analyse(request):
    return render(request, "analyse.html")
