
from django.http import HttpResponse
from django.shortcuts import render

from .database import creation_table


def admin_pollu(request): 
    return render(request, "admin_pollu.html")


def database(request): 
    return render(request, "database.html")

def prédiction(request): 
    return render(request, "prédiction.html")

def remplir_database(request): 
    return render(request, "remplir_database.html")




def construction(request):

    if request.method == "POST":
        try:
            creation_table()
        except:
            print('table déja crée')
        

    return render(request, "admin_pollu.html")
