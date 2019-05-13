from django.shortcuts import render
import os
import cv2

from .analysis_psychopg2.mode_analyse import *
from .analysis_psychopg2.coupe_analysis import *

from .analysis_psychopg2.mode_w_data import haut_bas

from django.core.files import File

from .models import *
from .forms import imagepost


def mode(request):
    return render(request, "mode.html")


def database_mode(request):

    data = recup()
    data_coupe = recup2()
    
    #print(data)
    print('ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

    #print(data_coupe)
    data2 = haut_bas()

    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
    liste = os.listdir()

    liste1 = []
    
    c = 0
    for i in liste:
        try:
            liste1.append((str(liste[c]), str(liste[c+1]), int(str(c) + str(c))))
            c+=2

        except:
            pass
    print(liste1)
    return render(request, "database_mode.html", {'data':data, 'data2':data2,
                                                  'data_coupe':data_coupe,
                                                  'image_hab':liste1})


def tendance(request):
    
    if request.method == "POST":
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")

        
    return render(request, "tendance.html")

def ajout(request):

    print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
    form = imagepost(request.POST or None, request.FILES or None)
    if form.is_valid():
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
        im = form.save(commit=False)
        im.save()
        print('saved')
    else:
        print("nononono")

        
    context = {'form':form}
    
    return render(request, "essais.html", context)

def analyse(request):
    return render(request, "analyse.html")


def essais(request):
    return render(request, "essais.html")













