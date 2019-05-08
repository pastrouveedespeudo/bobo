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


        image = capture(current_user, format_image)
        
        if format_image == "cheveux":
            os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\cheveux'.format(str(current_user)))
            cropage_cheveux(image, current_user)
            
        elif format_image == "habit":
            os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\habit'.format(str(current_user)))
            cropage_habit(image, current_user)


        liste_usr = []
        image = Accounts.objects.filter(name=current_user).all()
        for i in image:
            liste_usr.append(i.photo)

        return render(request, 'mes_images.html', {'usr':current_user, 'liste':liste_usr})


    return render(request, 'photo.html')



def essais(request):
    return render(request, 'essais.html')

def coupe(request):

    no_choice = 'no_choice'


    if request.method == "POST":
        
        image = request.POST.get('posting')

        if image:
            no_choice = ''
            print(image,"0100000000000000000000000000000000000")
            current_user = request.user
        
            return render(request, 'coupe.html', {'image':image, 'user':current_user})




    



    return render(request, 'coupe.html', {'no_choice':no_choice})

def habits(request):
    return render(request, 'habits.html')
















