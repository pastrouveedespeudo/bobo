
from django.http import HttpResponse
from django.shortcuts import render

from .polution.database2 import creation_table
from .polution.database2 import clean_data


from .polution.main import météologie
from .polution.main import climat
from .polution.main import pollution
from .polution.main import sociologie
from .polution.main import trafic_routier
from .polution.main import particule_plage
from .polution.main import particulee





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
        voir = request.POST.get('Voir')
        print(voir)
        if voir:
            data = ''
            return HttpResponse(data)

        
    return render(request, "database.html")

def prédiction(request): 
    return render(request, "prédiction.html")




def construction(request):

    if request.method == "POST":
        print('ouiiiiiiiiiiiiiiiiiiiiiiiii')
        try:
            creation_table()
        except:
            print('table déja crée')
        

    return render(request, "admin_pollu.html")
