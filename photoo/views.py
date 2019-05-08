from django.shortcuts import render

from .photo import *
from .coupenom import *
import os
from accounts.models import Accounts


def mes_images(request):
    return render(request, 'mes_images.html')

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
        

        os.chdir(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo")
        liste = os.listdir()
        #print(liste)
        
##        a = liste[0]
##        b = liste[1]
##        c = liste[2]
##        d = liste[3]
##        e = liste[4]
##        f = liste[5]


        #acc = Accounts.objects.get(name=current_user)
        #a = acc.photo
        #print(a.path)

        return render(request, 'mes_images.html')
##        return render(request, 'mes_images.html', {'capture':capturee,
##                                                   'a':a,'b':b,'c':c,
##                                                   'd':d,'e':e,'f':f } ) 

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
















