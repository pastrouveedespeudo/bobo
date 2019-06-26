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

from .coupe_dico import DICO_COIF

from .analysis.database import *


from .views_functions import the_colors_function
from .views_functions import gymm_map_function
from .views_functions import gymm_function
from .views_functions import haircut_style_function
from .views_functions import map_hairdresser_function


def navebarre_coupe(request):
    """Here we return a home html respons"""
    return render(request, 'navebarre_coupe.html')

def navebarre_habits(request):
    """Here we return a home html respons"""
    return render(request, 'navebarre_habits.html')

def home_bobo(request):
    """Here we return a home html respons"""
    return render(request, 'home_bobo.html')

def home(request):
    """Here we return a home html respons"""
    return render(request, 'home.html')


def coupe(request):
    """this is the interraction between
    the view and the template hair"""
    
    no_choice = 'no_choice'
    

    try:
        fav = '' 
        current_user = request.user
        favorites_haircut = displaying_favorite_haircut(current_user)#from photo.py
        if favorites_haircut:
            fav = True
    except:
        pass

 
    if request.method == "POST":

        #
        image = request.POST.get('posting')
        haircut = request.POST.get('coupe')
        search = request.POST.get('coupedecheveux')
        saving = request.POST.get('product')

        map_hairdresser = request.POST.get('buttony')
        vivile = request.POST.get('country')
        haircut_style = request.POST.get('hairdresser')

        gymm = request.POST.get('gymnastic')
        gymm_map = request.POST.get('buttony_gym')
        gym_pays = request.POST.get('country_gym')


        if gymm_map:

            #We call gymm_map_function from views_function
            data = gymm_map_function(gymm_map, gym_pays)
            return HttpResponse(data)


        if gymm:

            #We call gymm_function from views_function
            gym_list = gymm_function(gymm)
            return HttpResponse(gym_list)



        if haircut_style:

            #We call haircut_style_function from views_function
            coif = haircut_style_function(haircut_style)
            return HttpResponse(coif)

        
        if map_hairdresser:
            #We call map_hairdresser_function from views_function
            data = map_hairdresser_function(map_hairdresser, vivile)
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






def habits(request):
    """Here we calling function of views_functions
    we define the mode from informations
    from database.
    After traiting image"""
    
    if request.method == "POST":
        
        color = request.POST.get('a')
        draggable = request.POST.get('b')
        image_to_vet = request.POST.get('posting2')

        if image_to_vet:
            current_user = request.user

            return render(request, 'habits.html',
                          {'image_to_vet':image_to_vet,
                           'user':current_user})

        if color:

            color = color.split()
            color = color[-1]

            coul_analyse_haut, coul_analyse_bas = the_colors_function(color)

            return HttpResponse((coul_analyse_haut,' ', coul_analyse_bas))


            
    return render(request, 'habits.html')


















