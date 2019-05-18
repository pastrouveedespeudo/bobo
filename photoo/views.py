from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse
from .photo import *
from .coupenom import *
import os
from accounts.models import Accounts

from .coupe_dico import DICO_COIF

from .analysis.database import *

try:
    from static.bobo.tendance import *
except:
    pass


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
    
    try:
        current_user = request.user

        fav = ''#ICIIIIIII IL Y A PEUT ETRE UNE ERREUR c ptetre [] 
        favoris_coupe = affichage_coupe_fav(current_user)
        print(favoris_coupe)
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
 
        print(recherche,'7777777777777777777777777778888')
        print(coupe,'656565656565699999999789111111111117777')
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
















