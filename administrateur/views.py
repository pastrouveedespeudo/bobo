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

    try:
        liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
        for i in liste:
            print(i)

        nb = int(liste[-2][0]) + 1
        nouveau = str(nb) +  liste[-2][-4:]
        
        print(nouveau)

    except:
        liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
        print(liste)
        nouveau=''

    if request.method == "POST":
        mode = request.POST.get('hidden')
        print(mode,'000000000000000000000000000000000000000000000000')
        
    print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
    form = imagepost(request.POST or None, request.FILES or None)
    if form.is_valid():
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiii")
        im = form.save(commit=False)
        im.save()
        print('saved')
        

        liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
        img = cv2.imread(liste[-1])
        cv2.imwrite(nouveau, img)

        print('renamed')
        #coupe ? habit? avec un request

        
    else:
        print("nononono")

        
    context = {'form':form}
    
    return render(request, "ajout.html", context)

def analyse(request):
    return render(request, "analyse.html")


def essais(request):
    return render(request, "essais.html")













