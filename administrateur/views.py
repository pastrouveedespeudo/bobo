from django.shortcuts import render
import os


from .analysis_psychopg2.mode_analyse import *



def mode(request):
    return render(request, "mode.html")


def database_mode(request):

    data = recup()
    print(data)
    print('ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

    return render(request, "database_mode.html", {'data':data})


def tendance(request):
    return render(request, "tendance.html")

def ajout(request):
    return render(request, "ajout.html")

def analyse(request):
    return render(request, "analyse.html")
