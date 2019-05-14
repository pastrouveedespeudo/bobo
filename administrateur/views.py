from django.shortcuts import render
import os
import cv2

import json
from django.http import HttpResponse

from .analysis_psychopg2.mode_analyse import *
from .analysis_psychopg2.coupe_analysis import *

from .analysis_psychopg2.mode_w_data import haut_bas

from .analysis_psychopg2.analyse_femme_haut import traitement

from django.core.files import File

from .models import *
from .forms import imagepost

from django.http import JsonResponse

def mode(request):
    return render(request, "mode.html")


def database_mode(request):

    if request.method == "POST":
        print('databaseeeeeeeeeedatabaseeeeeeeeee')
        database = request.POST.get('database')
        print('databaseeeeeeeeee', database)
        dataaa = 'coucouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
        print(dataaa)
        return HttpResponse(dataaa)


    print('yoooooooooooooooooooooo')




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


    form = imagepost(request.POST or None, request.FILES or None)
    context = {'form':form}


    if request.method == "POST":
        mode = request.POST.get('hidden')
        print(mode,'777777777777777777777777777777777777777777777')
        liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
        
        liste_max = []

        
        for i in liste:
            print(i)
        
            try:
                print(str(i[0]) + str(i[1]))
                a = str(i[0]) + str(i[1])
                a = int(a)
                print(a,'8888888888888888888888888888888888888')
                liste_max.append(a)
                
            except:
                a = str(i[0])
                a = int(a)
                liste_max.append(a)
        
        print(liste_max,'000000000000000000000000000000')

        num = max(liste_max)

        new_number = int(num) + 1
        print(new_number)

        if mode == 'vetement':
            nouveau = str(new_number) + 'a.jpg'
            
        elif mode == 'coupe':
            num = max(liste_max)
            new_number = int(num)
            nouveau = str(new_number) + 'b.jpg'

        if form.is_valid():
            im = form.save(commit=False)
            im.save()
            
            liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
            os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
            img = cv2.imread(liste[-1])
            cv2.imwrite(nouveau, img)

            os.remove(liste[-1])
            print('renamed')
            
        return render(request, "mode.html", context)


    
    return render(request, "ajout.html", context)






def analyse(request):

    if request.method == "POST":
        print("ouiiiiiiiiiiiiiiiiiiiiiii")

        traitement()
       
        #image_femme_haut.traitement()
        
    return render(request, "analyse.html")


def essais(request):
    return render(request, "essais.html")













