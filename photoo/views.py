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



@csrf_protect
def coupe(request):

    no_choice = 'no_choice'
    
    try:
        current_user = request.user

        fav = '' 
        favoris_coupe = affichage_coupe_fav(current_user)
        #print(favoris_coupe)
        if favoris_coupe:
            fav = True


    except:
        pass
    
    if request.method == "POST":

        

        print('OUIIIIIIIIIIIII')
        image = request.POST.get('posting')
        coupe = request.POST.get('coupe')
        recherche = request.POST.get('coupedecheveux')
        enregistement = request.POST.get('produit')
    
        numero_coiffeur = request.POST.get('numero_coiffeur')
        vivile = request.POST.get('country')

        
        coiffure = request.POST.get('coiffeur')
        MON_COIFFEUR = []
        
        print(coiffure,'000000000000000000000000000')
        print(numero_coiffeur,'000000000000000000000000000chicha')
        print(vivile)

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
                
            print(liste,'000000000000000000048787/')

            num  = []
            for i in liste:
                a = numero(i, vivile)
                num.append([a])

            return HttpResponse(num)






        c = 0
        if coiffure:

            coif = []
          
            les_coiffeurs = ville(coiffure)
            #for i in les_coiffeurs:
            #    print(i)


            
            MON_COIFFEUR.extend(les_coiffeurs)
  

            
                
            for i in MON_COIFFEUR:
                

                horraire1 = horraire(i, coiffure)
                print(i)
                print(horraire1)
             
                if [horraire1] == [] or horraire1 == []\
                   or horraire1 == "" or horraire1 == " "\
                   or horraire1 == None:
                    MON_COIFFEUR.remove(i)
                    
                else:
                    coif.append([i, horraire1, ""])
                    MON_COIFFEUR.remove(i)
                
       
            
              
                

            #print(coif)
            #print('iciiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            return HttpResponse(coif)
 


        
        

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
            print('RECHERHCEEEEEEEEEEEEEEEEEEEEE', recherche)
            for cle, value in DICO_COIF.items():
                pass
            
            return render(request, 'habits.html', {'recherche':recherche})



        
        if image:
            no_choice = ''
            print(image,"0100000000000000000000000000000000000")
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


        if coupe:
            print(coupe,'pppppppppppppppppppppppppppppppppp')



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

        print(couleur, draggable, '0000000000000000000000000000000000000')
        print(image_to_vet,'000000000000000000000000000000000000000000000')


    
        if image_to_vet:
            
            print('pouoioioioioioioioioioioioioioioioioioioioioioioioioioioioioi')
            print('ouaiiiiiiiiiiiiiiiiiiiiiiiis')
            print(image_to_vet)
            
            current_user = request.user


            
            return render(request, 'habits.html', {'image_to_vet':image_to_vet,
                                                   'user':current_user})


        if draggable:
            pass

        if couleur:
            print('oui')

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

            print(liste10,'0000000000000000000000000')
    
            if couleur == 'blonde':
                print(liste10[1], '1111111111111111111111111111')

                coul_analyse_haut = liste10[1][0]
                coul_analyse_bas = liste10[1][1]
                 
            elif couleur == 'brune' or couleur == 'noire':
                print(liste10[0],  '1111111111111111111111111111')
                
                coul_analyse_haut = liste10[0][0]
                coul_analyse_bas = liste10[0][1]

            elif couleur == 'chatain' or couleur == 'rousse':
                print(liste10[2], '1111111111111111111111111111')
                
                coul_analyse_haut = liste10[2][0]
                coul_analyse_bas = liste10[2][1]

            print(coul_analyse_haut)
            print(coul_analyse_bas)

            return HttpResponse((coul_analyse_haut,' ', coul_analyse_bas))


            
    return render(request, 'habits.html')


















