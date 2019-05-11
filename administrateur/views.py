from django.shortcuts import render
import os

def mode(request):
    return render(request, "mode.html")


def database_mode(request):

    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\administrateur\analysis_psychopg2')
    liste = os.listdir()

    for i in liste:
        if i == '__pycache__' or i == 'analyse_femme_haut.py' or\
           i == 'constante.py' or i == 'coul.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
           i=='bobo.txt' or i== 'traitement_haut.jpg' or i == "traitement_bas1.jpg" or\
           i == 'config.py' or i == 'constante.py' or i =='coul.py' or i == 'database.py' or\
           i == 'palettecouleur.py' or i =='palettecouleur_coiffure.py':
            pass

        else:
            print(i)
    
    return render(request, "database_mode.html")


def tendance(request):
    return render(request, "tendance.html")

def ajout(request):
    return render(request, "ajout.html")

def analyse(request):
    return render(request, "analyse.html")
