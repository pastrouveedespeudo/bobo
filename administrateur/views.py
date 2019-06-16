import os
import cv2
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from django.http import JsonResponse

from .models import *
from .forms import imagepost


from static.bobo.coupe_analysis import *
from static.bobo.mode_analyse import *

from .tendance_site.mode_w_data import *


try:
    from static.bobo.tendance import *
except:
    pass


def database_mode(request):

    data = recup()#from mode_analyse.py
    data_coupe = recup2()#from coupe_analysis
    data2 = haut_bas()#from mode_w_data

    try:
        os.chdir('/app/static/bobo')
    except:
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')


    liste = os.listdir()

    liste1 = []
    liste11 = []
    theliste1 = []

    #We ignore this files
    #or add it to laliste
    for i in liste:
        if i == 'analyse_femme_haut.py' or  i == 'bobo.txt' or\
           i == 'config.py' or i == 'constante.py' or i == 'conteneur.py' or\
           i == 'coul.py' or i == 'coupe_analysis.py' or i=='constante.py' or\
           i == 'database.py' or i == 'mode_analyse.py' or i == 'mode_w_data.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
           i == 'traitement_bas1.jpg' or i == 'traitement_haut.jpg' or i == '__pycache__' or i=='bobo.txt'\
           or i =='analysa.py' or i == 'tendance.py':
            pass
        else:
            theliste1.append(i)

    theliste1 = sorted(theliste1)

    #We add picture,
    c = 0
    for i in theliste1:
        try:
            liste1.append((str(laliste1[c]), str(laliste1[c+1]), int(str(c) + str(c))))
            c+=2
        except:
            pass
        
    try:
        os.chdir('/app/static/bobo')
    except:
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')

    listee = os.listdir()
    
    c = 0
    for i in theliste1:

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
    print(liste1)

    return render(request, "database_mode.html", {'data':data, 'data2':data2,
                                                  'data_coupe':data_coupe,
                                                  'image_hab':liste1,
                                                  'final':liste_finale,
                                                  'laliste1':laliste1,
                                                  'blond':blond, 'brun':brun, 'chatain':chatain})


def tendance(request):
    
    try:
        os.chdir('/app/static/bobo')
    except:
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
           or i =='analysa.py' or i =='tendance.py':
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
    
 
    liste = dataaa()
    liste1 = i_into_i(liste)
    liste2 = unification(liste1)
    liste3 = suppression_en_trop(liste2)
    liste6 = re_elment_de_liste(liste3)
    liste7 = mise_en_dico(liste6)
    liste8 = determination_couleur(liste7)
    liste9 = les_tendances_couleurs(liste8)
    liste10 = analyse_tendance(liste9)
    #brun, blond, chatain


    return render(request, "tendance.html", {'blond':blond, 'brun':brun,
                                             'chatain':chatain,
                                             'liste10':liste10, 'coupa':coupa})



















