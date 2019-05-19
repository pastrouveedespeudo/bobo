
from django.http import HttpResponse
from django.shortcuts import render

from .database import creation_table





def remplir_database(request):

    if request.method == "POST":
        print('ouiiiiiiiiiiiii')
        remplir = request.POST.get('remplissage')
        verif = request.POST.get('verification')
        delete = request.POST.get('delete')


        
        print(remplir)

        if remplir:
            pass
        if verif:
            print('ouiiiiiiiii')

        if delete:
            print('deeeeeeeeelte')

        
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
