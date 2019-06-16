
#Django Stuff
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.http import StreamingHttpResponse
from django.middleware.gzip import GZipMiddleware


import os
import cv2


from accounts.models import Accounts

from .photo import *
from .photo import displaying_favorite_haircut
from .coupenom import *

from .coupe_dico import DICO_COIF

from .analysis.database import *

try:
    from static.bobo.tendance import *
except:
    pass





#Section searching hairdresser, gym
from .magasins.hairdresser import *
from .magasins.address import *
from .magasins.gym import *


def home_bobo(request):
    """Here we return a home html respons"""
    return render(request, 'home_bobo.html')

def home(request):
    """Here we return a home html respons"""
    return render(request, 'home.html')

@csrf_exempt
def coupe(request):
    """this is the interraction between
    the view and the template hair"""
    
    no_choice = 'no_choice'
    
   
    #here we look if the user has favorites,
    #if yes we return true with fav variable

    try:
        fav = '' 
        current_user = request.user
        #from photo.py
        favorites_haircut = displaying_favorite_haircut(current_user)
        if favorites_haircut:
            fav = True
    except:
        pass

 
    if request.method == "POST":

        image = request.POST.get('posting')
        haircut = request.POST.get('coupe')
        search = request.POST.get('coupedecheveux')
        saving = request.POST.get('product')

        map_hairdresser = request.POST.get('buttony')#city for hairdresser
        number_hairdresser = request.POST.get('numero_coiffeur')#number phone for hairdresser
        vivile = request.POST.get('country')#city for hairdresser map
        haircut_style = request.POST.get('hairdresser')#this is request for a hairdress

        gymm = request.POST.get('gymnastic')#this is request for a gym
        gymm_map = request.POST.get('buttony_gym')#this is country for map gym
        gym_pays = request.POST.get('country_gym')#this is country for search gym


        MY_HAIRDRESSER = []
        
        if gymm_map:#if user call the gym card
            the_address = address_geo(gymm_map, gym_pays)#we search the address by scrapping
            
            try:
                lat_long = city_geo(la_adresse)#and recup it with nominatim (with lat et long)
            except:
                return HttpResponse("Oups nous n'avons rien trouvé")#if nothing is found we return it

            data = str(lat_long[0]) + ' ' + str(lat_long[1])#if no exception, we traiting data for js code
            #we add a space 
     
            if data == ' ' or data == '':
                return HttpResponse("Oups nous n'avons rien trouvé")#for sure we return again an exception
            
            return HttpResponse(data)#if no exception, we return data on page


        if gymm:#if user call the gym location
            gym_list = []

            the_cities = big_city_gym(gymm)
            
            for i in the_cities:
                
                if len(gym_liste) == 4:
                    return HttpResponse(gym_liste)
                    
                a = schedule_gym(i, gymm)

                if a != []:
                    gym_list.append([i, a, ""])
            

            return HttpResponse(gym_list)


        c = 0
        if haircut_style:

            coif = []
          
            the_hairdressers = cities(haircut_style)

            MY_HAIRDRESSER.extend(the_hairdressers)

            for i in MY_HAIRDRESSER:
                
                schedule1 = schedule_hair(i, haircut_style)
 
             
                if [schedule1] == [] or schedule1 == []\
                   or schedule1 == "" or schedule1 == " "\
                   or schedule1 == None:
                    MY_HAIRDRESSER.remove(i)
                    
                else:
                    coif.append([i, schedule1, ""])
                    MY_HAIRDRESSER.remove(i)


            return HttpResponse(coif)
 

        if number_hairdresser and vivile:
            liste = []

            coif = ''
            for i in number_hairdresser:
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


        
        if map_hairdresser:
            the_address = address_geo(map_hairdresser, vivile)
            try:
                lat_long = city_geo(the_address)
            except:
                return HttpResponse('Oups nous n\'avons rien trouvé')

            data = str(lat_long[0]) + ' ' + str(lat_long[1])
            
            if data == ' ' or data == '':
                return HttpResponse('Oups nous n\'avons rien trouvé')

            return HttpResponse(data)



        liste_enre = [[],[],[]]
        c = 0
        if saving:
            for i in saving:
                if i == ',':
                    c+=1
                else:
                    liste_enre[c].append(i)

            
            coupe_fav(current_user, "".join(liste_enre[0]),
                      "".join(liste_enre[1]),
                      "".join(liste_enre[2]))
            

        if search:
            for key, value in DICO_COIF.items():
                pass
            
            return render(request, 'habits.html', {'recherche':recherche})



        
        if image:
            no_choice = ''
            current_user = request.user
            
            try:
                if fav == True:
                    return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                          'coif':favorites_haircut})
                else:
                    return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                          'fav':fav})
                
            except:
                return render(request, 'coupe.html', {'image':image, 'user':current_user})


    try:
        if fav == True:
            return render(request, 'coupe.html', {'no_choice':no_choice,
                                                  'coif':favorites_haircut})

        else:
            return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                          'fav':fav})
        
    except:
        return render(request, 'coupe.html', {'no_choice':no_choice})





@csrf_exempt
def habits(request):

    if request.method == "POST":
        
        color = request.POST.get('a')
        draggable = request.POST.get('b')
        image_to_vet = request.POST.get('posting2')

        if image_to_vet:
            current_user = request.user


            
            return render(request, 'habits.html', {'image_to_vet':image_to_vet,
                                                   'user':current_user})


        if draggable:
            pass

        if color:

            color = color.split()
            color = color[-1]

            liste = dataaa()
            liste1 = i_into_i(liste)
            liste2 = unification(liste1)
            liste3 = suppression_en_trop(liste2)
            liste6 = re_elment_de_liste(liste3)
            liste7 = mise_en_dico(liste6)
            liste8 = determination_couleur(liste7)
            liste9 = les_tendances_couleurs(liste8)
            liste10 = analyse_tendance(liste9)

    
            if color == 'blonde':
                coul_analyse_haut = liste10[1][0]
                coul_analyse_bas = liste10[1][1]
                 
            elif color == 'brune' or couleur == 'noire':
                coul_analyse_haut = liste10[0][0]
                coul_analyse_bas = liste10[0][1]

            elif color == 'chatain' or couleur == 'rousse':
                
                coul_analyse_haut = liste10[2][0]
                coul_analyse_bas = liste10[2][1]


            return HttpResponse((coul_analyse_haut,' ', coul_analyse_bas))


            
    return render(request, 'habits.html')


















