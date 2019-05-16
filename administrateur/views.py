from django.shortcuts import render
import os
import cv2

import json
from django.http import HttpResponse


try:
    from static.bobo.analysa import *
except:
    pass

from django.core.files import File

from .models import *
from .forms import imagepost

from django.http import JsonResponse

from static.bobo.mode_w_data import haut_bas
from static.bobo.coupe_analysis import *
from static.bobo.mode_analyse import *
from static.bobo.analyse_femme_haut import *

def mode(request):
       
    return render(request, "mode.html")


def database_mode(request):

    if request.method == "POST":
        return HttpResponse('ok')

    data = recup()#from mode_analyse.py
    data_coupe = recup2()#from coupe_analysis
    data2 = haut_bas()#from mode_w_data

    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
    liste = os.listdir()

    liste1 = []
    laliste1 = []

    for i in liste:
        if i == 'analyse_femme_haut.py' or  i == 'bobo.txt' or\
           i == 'config.py' or i == 'constante.py' or i == 'conteneur.py' or\
           i == 'coul.py' or i == 'coupe_analysis.py' or i=='constante.py' or\
           i == 'database.py' or i == 'mode_analyse.py' or i == 'mode_w_data.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
           i == 'traitement_bas1.jpg' or i == 'traitement_haut.jpg' or i == '__pycache__' or i=='bobo'\
           or i =='analysa.py':
            pass
        else:
            laliste1.append(i)



    c = 0
    for i in laliste1:
        try:
            liste1.append((str(laliste1[c]), str(laliste1[c+1]), int(str(c) + str(c))))
            c+=2
        except:
            pass
        



    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
    listee = os.listdir()
    
    liste11 = []
    
    c = 0
    for i in laliste1:

        try:
            liste11.append((str(laliste1[c]), str(laliste1[c+1]), int(str(c) + str(c))))
            c+=2
        except:
            pass


    
    a = haut_bas()
 
    b = recup2()
 
    c = liste11

    liste_finale = []

    compteur = 0
    if len(a) == len(b) == len(c):
        for i in a:
            liste_finale.append(([c[compteur], b[compteur], a[compteur][0], a[compteur][1]]))

            compteur += 1
            
    coupa = []
    for i in data_coupe:
        coupa.append(i[2])
    
        
    brun = coupa.count('marron')
    chatain = coupa.count('chatin')
    blond = coupa.count('blond')


    return render(request, "database_mode.html", {'data':data, 'data2':data2,
                                                  'data_coupe':data_coupe,
                                                  'image_hab':liste1, 'final':liste_finale,
                                                  'blond':blond, 'brun':brun, 'chatain':chatain})


def tendance(request):
    
    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
    liste = os.listdir()

    liste1 = []
    
    c = 0
    laliste1 = []
    for i in liste:
        if i == 'analyse_femme_haut.py' or i == 'bobo.txt'\
           or i == 'config.py' or i == 'constante.py' or i ==  'conteneur.py'\
           or i == 'coul.py' or i ==  'coupe_analysis.py'\
           or i == 'database.py' or i ==  'mode_analyse.py' or i ==  'mode_w_data.py'\
           or i == 'palettecouleur.py'  or i ==  'palettecouleur_coiffure.py'\
           or i == 'traitement_bas1.jpg'  or i ==  'traitement_haut.jpg' or i == '__pycache__'\
           or i =='analysa.py':
            pass
        else:
            laliste1.append(i)



    for i in laliste1:
        try:
            liste1.append((str(laliste1[c]), str(laliste1[c+1]), int(str(c) + str(c))))
            c+=2

        except:
            pass
            
    data2 = haut_bas()
    data_coupe = recup2()
    #liste1
    
    coupa = []
    for i in data_coupe:
        coupa.append(i[2])
      
    brun = coupa.count('marron')
    chatain = coupa.count('chatin')
    blond = coupa.count('blond')
    try:
        liste_ana = analysa()#haut, bas, brun, 1a.jpg
        liste_tendance = les_tendances_couleurs()
    except:
        liste_ana = ''
        liste_tendance= ''



    return render(request, "tendance.html", {'blond':blond, 'brun':brun, 'chatain':chatain,
                                             'liste_ana':liste_ana, 'liste_tendance':liste_tendance})








def ajout(request):


    form = imagepost(request.POST or None, request.FILES or None)
    context = {'form':form}

    try:
        if request.method == "POST":
            mode = request.POST.get('hidden')

            liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')
            
            liste_max = []

            
            for i in liste:
                print(i)
            
                try:
                    print(str(i[0]) + str(i[1]))
                    a = str(i[0]) + str(i[1])
                    a = int(a)
                
                    liste_max.append(a)
                    
                except:
                    a = str(i[0])
                    a = int(a)
                    liste_max.append(a)
            
         

            num = max(liste_max)

            new_number = int(num) + 1
        

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
    except:
        pass

    
    return render(request, "ajout.html", context)






def analyse(request):

    if request.method == "POST":
        print("ouiiiiiiiiiiiiiiiiiiiiiii")
        traitement()
       
        try:
            analysa()
            les_tendances_couleurs()
        except:
            pass
    return render(request, "analyse.html")


def essais(request):
    return render(request, "essais.html")













