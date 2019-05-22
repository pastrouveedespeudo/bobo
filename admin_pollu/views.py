
from django.http import HttpResponse
from django.shortcuts import render

from .polution.database2 import creation_table
from .polution.database2 import clean_data
from .polution.database2 import clean_data2
from .polution.database2 import clean_data3
from .polution.database2 import clean_data4
from .polution.database2 import visualisation

from .polution.main import météologie
from .polution.main import climat
from .polution.main import pollution
from .polution.main import sociologie
from .polution.main import trafic_routier
from .polution.main import particule_plage
from .polution.main import particulee

from .polution.traitement_de_donnée import condition
from .polution.traitement_de_donnée import recuperation_data


def remplir_database(request):

    if request.method == "POST":
        print('ouiiiiiiiiiiiii')
        remplir = request.POST.get('remplissage')
        verif = request.POST.get('verification')
        delete = request.POST.get('delete')


        
        print(remplir)

        if remplir:
            
            météologie()
            climat()       
            pollution()
            sociologie()
            trafic_routier()
            particulee()
            particule_plage()

            data = {'data':'fin data rempli'}


        if verif:
            clean_data()
            print('ouiiiiiiiii')


        
    return render(request, "remplir_database.html")



def admin_pollu(request): 
    return render(request, "admin_pollu.html")


def database(request):
    
    if request.method == "POST":
        print('ouiiiiiiiiiiiii')
        clean_data()
        clean_data2()
        clean_data3()
        clean_data4()
        paris = request.POST.get('paris')
        lyon = request.POST.get('lyon')
        marseille = request.POST.get('marseille')
        print(marseille, paris, lyon)

        
        if marseille:
            data = visualisation('marseille')
            liste = []

            for i in data:
                liste.append(i)
                liste.append('<br><br>')
                
            return HttpResponse(liste)

        
        if lyon:
            data = visualisation('lyon')
            liste = []

            for i in data:
                liste.append(i)
                liste.append('<br><br>')
                
            return HttpResponse(liste)

        
        if paris:
            data = visualisation('paris')
            liste = []

            for i in data:
                liste.append(i)
                liste.append('<br><br>')
                
            return HttpResponse(liste)

        
    return render(request, "database.html")





def prédiction(request):
    if request.method == "POST":
        print('coucouuuuuuuuuuu')
        
        prédiction = request.POST.get('prediction')
        if prédiction:
            clean_data()
            clean_data2()
            clean_data3()
            clean_data4()
            predi = []
            liste = ['paris', 'lyon', 'marseille']
            
            for i in liste:
                print(i)
                donnée = recuperation_data(i)
            
                pred = condition(donnée[0], donnée[1], donnée[2],
                        donnée[3], donnée[4], donnée[5], i)
                predi.append((i, pred))
            
            return HttpResponse(predi)
            
                
    return render(request, "prédiction.html")




def construction(request):

    if request.method == "POST":
        print('ouiiiiiiiiiiiiiiiiiiiiiiiii')
        try:
            creation_table()
        except:
            print('table déja crée')
        

    return render(request, "admin_pollu.html")



























