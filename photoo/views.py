from django.shortcuts import render
from .photo import *
import os

def mes_images(request):
    return render(request, 'mes_images.html')




def photo(request):
    if request.method == "POST":
        
        recherche = request.POST.get('im')
        print(recherche,"000000000000000000000000000000000000000000000000000")
        capturee = capture()
        print(capturee)
        cropage()
        os.chdir(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo")
        liste = os.listdir()
        print(liste)
        a = liste[0]
        b = liste[1]
        c = liste[2]
        d = liste[3]
        e = liste[4]
        f = liste[5]
        return render(request, 'mes_images.html', {'capture':capturee,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f }) 


    
    return render(request, 'photo.html')


def essais(request):
    return render(request, 'essais.html')

def coupe(request):
    if request.method == "POST":
        recherche = request.POST.get('coupedecheveux')
        print(recherche)
        print(recherche, "56666666666666666666666666666666666666666666")
    return render(request, 'coupe.html')




















