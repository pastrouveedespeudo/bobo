from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse
from .photo import *
from .coupenom import *
import os
from accounts.models import Accounts

from .coupe_dico import DICO_COIF

from .analysis.database import *
from django.middleware.gzip import GZipMiddleware
try:
    from static.bobo.tendance import *
except:
    pass

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.gzip import gzip_page
from django.http import StreamingHttpResponse

import cv2

from .magasins.coiffeur import *
from .magasins.adresse import *

from .magasins.gym import *


def home(request):
    """Here we return a home html respons"""
    return render(request, 'home.html')



@csrf_protect
def coupe(request):
    """this is the interraction between
    the view and the template hair"""
    
    no_choice = 'no_choice'
    
    try:
        """here we look if the user has favorites,
        if yes we return true with fav variable"""

        fav = '' 
        current_user = request.user
        favoris_coupe = affichage_coupe_fav(current_user)
        if favoris_coupe:
            fav = True
    except:
        pass
    
    if request.method == "POST":

        image = request.POST.get('posting')
        coupe = request.POST.get('coupe')
        recherche = request.POST.get('coupedecheveux')
        enregistement = request.POST.get('produit')

        map_coiffure = request.POST.get('buttony')#city for hairdresser
        numero_coiffeur = request.POST.get('numero_coiffeur')#number phone for hairdresser
        vivile = request.POST.get('country')#city for hairdresser map
        coiffure = request.POST.get('coiffeur')#this is request for a hairdress ?

        gymm = request.POST.get('gymnastique')#this is request for a gym ?
        gymm_map = request.POST.get('buttony_gym')#this is country for map gym
        gym_pays = request.POST.get('country_gym')#this is country for search gym


        MON_COIFFEUR = []
        
        if gymm_map:#if user call the gym card
            la_adresse = addresse_geo(gymm_map, gym_pays)#we search the address by scrapping
            
            try:
                lat_long = ville_geo(la_adresse)#and recup it with nominatim (with lat et long)
            except:
                return HttpResponse("Oups nous n'avons rien trouvé")#if nothing is found we return it

            data = str(lat_long[0]) + ' ' + str(lat_long[1])#if no exception, we traiting data
     
            if data == ' ' or data == '':
                return HttpResponse("Oups nous n'avons rien trouvé")#for sure we return again an exception
            
            return HttpResponse(data)#if no exception, we return data on page


        if gymm:#if user call the gym location
            gym_liste = []

            les_villes = grande_ville_gym(gymm)
            
            for i in les_villes:
                
                if len(gym_liste) == 4:
                    return HttpResponse(gym_liste)
                    
                a = horraire_gym(i, gymm)

                if a != []:
                    gym_liste.append([i, a, ""])
            

            return HttpResponse(gym_liste)


        c = 0
        if coiffure:

            coif = []
          
            les_coiffeurs = ville(coiffure)

            MON_COIFFEUR.extend(les_coiffeurs)

            for i in MON_COIFFEUR:
                
                horraire1 = horraire(i, coiffure)
 
             
                if [horraire1] == [] or horraire1 == []\
                   or horraire1 == "" or horraire1 == " "\
                   or horraire1 == None:
                    MON_COIFFEUR.remove(i)
                    
                else:
                    coif.append([i, horraire1, ""])
                    MON_COIFFEUR.remove(i)


            return HttpResponse(coif)
 

        if numero_coiffeur and vivile:
            liste = []

            coif = ''
            for i in numero_coiffeur:
                if i == ',':
                    liste.append(coif)
                    coif = ''
                else:
                    coif += i
                    
            liste.append(coif)
                


            num  = []
            for i in liste:
                a = numero(i, vivile)
                num.append([a])

            return HttpResponse(num)


        
        if map_coiffure:
            la_adresse = addresse_geo(map_coiffure, vivile)
            try:
                lat_long = ville_geo(la_adresse)
            except:
                return HttpResponse('Oups nous n\'avons rien trouvé')

            data = str(lat_long[0]) + ' ' + str(lat_long[1])
            
            if data == ' ' or data == '':
                return HttpResponse('Oups nous n\'avons rien trouvé')

            return HttpResponse(data)



        liste_enre = [[],[],[]]
        c = 0
        if enregistement:
            for i in enregistement:
                if i == ',':
                    c+=1
                else:
                    liste_enre[c].append(i)

            
            coupe_fav(current_user, "".join(liste_enre[0]),
                      "".join(liste_enre[1]),
                      "".join(liste_enre[2]))
            

        if recherche:
            for cle, value in DICO_COIF.items():
                pass
            
            return render(request, 'habits.html', {'recherche':recherche})



        
        if image:
            no_choice = ''
            current_user = request.user
            
            try:
                if fav == True:
                    return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                          'coif':favoris_coupe})
                else:
                    return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                          'fav':fav})
                
            except:
                return render(request, 'coupe.html', {'image':image, 'user':current_user})


    try:
        if fav == True:
            return render(request, 'coupe.html', {'no_choice':no_choice,
                                                  'coif':favoris_coupe})

        else:
            return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                          'fav':fav})
        
    except:
        return render(request, 'coupe.html', {'no_choice':no_choice})





@csrf_exempt
def habits(request):

    
    if request.method == "POST":
        
        couleur = request.POST.get('a')
        draggable = request.POST.get('b')
        image_to_vet = request.POST.get('posting2')

        if image_to_vet:
            current_user = request.user


            
            return render(request, 'habits.html', {'image_to_vet':image_to_vet,
                                                   'user':current_user})


        if draggable:
            pass

        if couleur:

            couleur = couleur.split()
            couleur = couleur[-1]

            liste = dataaa()
            liste1 = i_into_i(liste)
            liste2 = unification(liste1)
            liste3 = suppression_en_trop(liste2)
            liste6 = re_elment_de_liste(liste3)
            liste7 = mise_en_dico(liste6)
            liste8 = determination_couleur(liste7)
            liste9 = les_tendances_couleurs(liste8)
            liste10 = analyse_tendance(liste9)

    
            if couleur == 'blonde':
                coul_analyse_haut = liste10[1][0]
                coul_analyse_bas = liste10[1][1]
                 
            elif couleur == 'brune' or couleur == 'noire':
                coul_analyse_haut = liste10[0][0]
                coul_analyse_bas = liste10[0][1]

            elif couleur == 'chatain' or couleur == 'rousse':
                
                coul_analyse_haut = liste10[2][0]
                coul_analyse_bas = liste10[2][1]


            return HttpResponse((coul_analyse_haut,' ', coul_analyse_bas))


            
    return render(request, 'habits.html')


















