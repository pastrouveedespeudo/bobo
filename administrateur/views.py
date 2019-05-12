from django.shortcuts import render
import os


from .analysis_psychopg2.mode_analyse import *


from .analysis_psychopg2.mode_w_data import haut_bas


def mode(request):
    return render(request, "mode.html")


def database_mode(request):

    data = recup()
    data_coupe = recup2()
    
    print(data)
    print('ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

    data2 = haut_bas()


        
    return render(request, "database_mode.html", {'data':data, 'data2':data2,
                                                  'data_coupe':data_coupe})


def tendance(request):
    return render(request, "tendance.html")

def ajout(request):
    return render(request, "ajout.html")

def analyse(request):
    return render(request, "analyse.html")
