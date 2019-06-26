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

from .coupe_dico import DICO_COIF

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


    return render(request, 'coupe.html')





def habits(request):
    """Here we calling function of views_functions
    we define the mode from informations
    from database.
    After traiting image"""
    
    if request.method == "POST":
        
        color = request.POST.get('a')
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


















