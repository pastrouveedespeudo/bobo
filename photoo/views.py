from django.shortcuts import render

from .photo import *
from .coupenom import *
import os
from accounts.models import Accounts


def mes_images(request):
    current_user = request.user
    print(current_user)

    liste = []
    image = Accounts.objects.filter(name=current_user).all()
    for i in image:
        liste.append(i.photo)
    
    return render(request, 'mes_images.html', {'user':current_user, 'liste':liste})



def home(request):
    return render(request, 'home.html')

def tshirt(request):
    return render(request, 't-shirt.html')

def pantalon(request):
    return render(request, 'pantalon.html')



def photo(request):

    if request.method == "POST":
        
        format_image = request.POST.get('format')
        ordinom = request.POST.get('laprems')
        
        print(format_image,'4899999999999999999999999999999')
        print(ordinom,'4899999999999999999999999999999')
        
        current_user = request.user         
        print(current_user)
        if ordinom:
            nom_ordi(ordinom, current_user)


        image = capture(current_user)
        
        if format_image == "cheveux":
            cropage_cheveux(image, current_user)
        elif format_image == "habit":
            cropage_habit(image, current_user)
        

        return render(request, 'mes_images.html', {'usr':current_user})


    return render(request, 'photo.html')



def essais(request):
    return render(request, 'essais.html')

def coupe(request):

    if request.method == "POST":
        
        recherche = request.POST.get('coupedecheveux')
        print(recherche,"................................................")
        tenu = coupe_de_cheveux_nom(recherche)
        a = choix_fichier_haut(tenu[0])
        b = choix_fichier_haut(tenu[1])
        for i in a:
            return render(request, 'habits.html', {'a':a, 'b':b, "i":i} )

    
    return render(request, 'coupe.html')



def habits(request):
    return render(request, 'habits.html')
















