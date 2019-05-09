from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


from .photo import *
from .coupenom import *
import os
from accounts.models import Accounts

from .coupe_dico import DICO_COIF


def mes_images(request):
    
    current_user = request.user
    print(current_user)

    liste1 = []
    liste2 = []
    
    image = Accounts.objects.filter(name=current_user).all()
    for i in image:
        print(i.photo_habit, i.photo_cheveux)
        liste1.append(i.photo_habit)
        liste2.append(i.photo_cheveux)
        

    print(liste1)
    
    liste11 = []
    liste22 = []
    
    for i in liste1:
        if i == '':
            pass
        else:
            liste11.append(i)
            
    for i in liste2:
        if i == '':
            pass
        else:
            liste22.append(i)
            
    return render(request, 'mes_images.html', {'user':current_user, 'liste1':liste11,
                                               'liste2':liste22})



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
        coupe = request.POST.get('coupe')
        
        print(format_image,'4899999999999999999999999999999')

        current_user = request.user         
        print(current_user)


        image = capture(current_user, format_image)
        
        if format_image == "cheveux":
            os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\cheveux'.format(str(current_user)))
            cropage_cheveux(image, current_user, 'cheveux')
            
        elif format_image == "habit":
            os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\habit'.format(str(current_user)))
            cropage_habit(image, current_user, 'habit')

      
        liste1 = []
        liste2 = []
        
        image = Accounts.objects.filter(name=current_user).all()
        for i in image:
 
            liste1.append(i.photo_habit)
            liste2.append(i.photo_cheveux)

        liste11 = []
        liste22 = []
        
        for i in liste1:
            print(i)
            if i == '':
                pass
            else:
                liste11.append(i)
                
        for i in liste2:
            if i == '':
                pass
            else:
                liste22.append(i)
                
        return render(request, 'mes_images.html', {'user':current_user, 'liste1':liste11,
                                                   'liste2':liste22})


    return render(request, 'photo.html')



def essais(request):
    return render(request, 'essais.html')



@csrf_protect
def coupe(request):

    no_choice = 'no_choice'

    current_user = request.user
    
    affichage_coupe_fav(current_user)
    
    if request.method == "POST":

        print('OUIIIIIIIIIIIII')
        image = request.POST.get('posting')
        coupe = request.POST.get('coupe')
        recherche = request.POST.get('coupedecheveux')
        
        enregistement = request.POST.get('produit')
 
        print(recherche,'7777777777777777777777777778888')
        print(coupe,'777777777777777777777777777777')
        print(enregistement,'8888888888888897978979879878979')

        

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
            return render(request, 'habits.html')
        
        if image:
            no_choice = ''
            print(image,"0100000000000000000000000000000000000")
            current_user = request.user
        
            return render(request, 'coupe.html', {'image':image, 'user':current_user,
                                                  affichage_coupe_fav[0],
                                                  affichage_coupe_fav[1],
                                                  affichage_coupe_fav[2]}})
        


    return render(request, 'coupe.html', {'no_choice':no_choice,
                                          affichage_coupe_fav[0],
                                          affichage_coupe_fav[1],
                                          affichage_coupe_fav[2]})

def habits(request):
    return render(request, 'habits.html')
















