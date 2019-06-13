from django.shortcuts import render
from django.http import HttpResponse

import requests
import urllib.request
import datetime
from bs4 import *

from .graphe.graphique_bouchon import *
from .graphe.graphique_climat import *
from .graphe.graphique_heure import *
from .graphe.graphique_manif import *
from .graphe.graphique_météo import *
from .graphe.graphique_polution_condition import *
from .graphe.graphique_pression import *
from .graphe.graphique_saison import *
from .graphe.graphique_traffique import *
from .graphe.graphique_vent import *
from .graphe.graphique_ville import *
from .graphe.graphique_weekend import *
from .graphe.graphique_population import *

from.polu_ana.polution.traitement_de_donnée import recuperation_data
from.polu_ana.polution.traitement_de_donnée import condition

from .polu_ana.polution.database2 import *
from .donnée_site.pollution import *

from .donnée_site.angrais import *
from .donnée_site.diesel import *
from .donnée_site.eruption import *
from .donnée_site.incendie import *
from .donnée_site.jour_nuit import *
from .donnée_site.polenne import *


def home(request):
    return render(request, 'home.html')


def polution(request):

    return render(request, 'polution.html')



def charger(request):
    return render(request, 'charger.html')

def donnée(request):

    data_lyon = taux_particule('lyon')
    data_paris = taux_particule('paris')
    data_marseille = taux_particule('marseille')



    météo_lyon = temps_ville('lyon', 'météo')
    vent_lyon = temps_ville('lyon', 'vent')

    météo_paris = temps_ville('paris', 'météo')
    vent_paris = temps_ville('paris', 'vent')

    météo_marseille = temps_ville('marseille', 'météo')
    vent_marseille = temps_ville('marseille', 'vent')

    température_lyon = climat_ville('lyon')
    température_paris = climat_ville('paris')
    température_marseille = climat_ville('marseille')

    saison_actuelle =  saison()

    traffique_lyon = traffique('lyon')
    départ_routier_lyon = traffique_lyon[0] 
    heure_pointe_lyon = traffique_lyon[1] 
    regulier_jour_lyon = traffique_lyon[2] 
    non_pointe_lyon = traffique_lyon[3] 


    traffique_paris = traffique('paris')
    départ_routier_paris = traffique_paris[0] 
    heure_pointe_paris = traffique_paris[1] 
    regulier_jour_paris = traffique_paris[2] 
    non_pointe_paris = traffique_paris[3] 


    
    traffique_marseille = traffique('marseille')
    départ_routier_marseille = traffique_marseille[0] 
    heure_pointe_marseille = traffique_marseille[1] 
    regulier_jour_marseille = traffique_marseille[2] 
    non_pointe_marseille = traffique_marseille[3] 

    jour = habitude()

    classement_lyon = ville_pollué_classement('lyon')
    classement_paris = ville_pollué_classement('paris')
    classement_marseille = ville_pollué_classement('marseille')

    pole_lyon = region_industrielle('lyon')
    pole_paris = region_industrielle('paris')
    pole_marseille = region_industrielle('marseille')

    pression_lyon = pression_ville('lyon')
    pression_paris = pression_ville('paris')
    pression_marseille = pression_ville('marseille')

    manif_lyon = activité_execptionnelle('lyon')
    manif_paris = activité_execptionnelle('paris')
    manif_marseille = activité_execptionnelle('marseille')
    

    socio_lyon = socio('lyon')
    socio_paris = socio('paris')
    socio_marseille = socio('marseille')

    bouchons_lyon = bouchons('lyon')
    bouchons_paris = bouchons('paris')


    errup = eruption()
    
    diesel = recup_balise()
    dollard = cours_dollar()
    
    incendie_lyon = incendie('lyon')
    incendie_marseille = incendie('marseille')
    incendie_paris = incendie('paris')

    angrais = periode_angrais()

    periode = nuit_jour()


    po_lyon = polenne('lyon')
    po_marseille = polenne('marseille')
    po_paris = polenne('paris')





    return render(request, 'donnée.html', {'lyon':data_lyon,
                                           'paris':data_paris,
                                           'marseille':data_marseille,
                                           'météo_lyon':météo_lyon,
                                           'météo_marseille':météo_marseille,
                                           'météo_paris':météo_paris,
                                           'vent_lyon':vent_lyon,
                                           'vent_paris':vent_paris,
                                           'vent_marseille':vent_marseille,
                                           'température_lyon':round(température_lyon),
                                           'température_paris':round(température_paris),
                                           'température_marseille':round(température_marseille),
                                           'saison_actuelle':saison_actuelle,
                                           'départ_routier_lyon':départ_routier_lyon,
                                           'heure_pointe_lyon':heure_pointe_lyon,
                                           'regulier_jour_lyon':regulier_jour_lyon,
                                           'non_pointe_lyon':non_pointe_lyon,
                                           'départ_routier_paris':départ_routier_paris,
                                           'heure_pointe_paris':heure_pointe_paris,
                                           'regulier_jour_marseille':regulier_jour_marseille,
                                           'non_pointe_marseille':non_pointe_marseille,
                                           'départ_routier_paris':départ_routier_paris,
                                           'heure_pointe_paris':heure_pointe_paris,
                                           'regulier_jour_paris':regulier_jour_paris,
                                           'non_pointe_paris':non_pointe_paris,
                                           'weekend':jour[0],
                                           'jour_semaine':jour[1],
                                           'classement_lyon':classement_lyon,
                                           'classement_paris':classement_paris,
                                           'classement_marseille':classement_marseille,
                                           'pole_lyon':pole_lyon,
                                           'pole_paris':pole_paris,
                                           'pole_marseille':pole_marseille,
                                           'pression_lyon':pression_lyon,
                                           'pression_paris':pression_paris,
                                           'pression_marseille':pression_marseille,
                                           'manif_lyon':manif_lyon,
                                           'manif_paris':manif_paris,
                                           'manif_marseille':manif_marseille,
                                           'socio_lyon':socio_lyon,
                                           'socio_marseille':socio_marseille,
                                           'socio_paris':socio_paris,
                                           'bouchons_lyon':bouchons_lyon,
                                           'bouchons_paris':bouchons_paris,
                                           'eruption':errup,
                                           'diesel':diesel,
                                           'dollard':dollard,
                                           'incendie_lyon':incendie_lyon,
                                           'incendie_marseille':incendie_marseille,
                                           'incendie_paris':incendie_paris,
                                           'angrais':angrais,
                                           'periode':periode,
                                           'po_lyon':po_lyon,
                                           'po_paris':po_paris,
                                           'po_marseille':po_marseille})


    return render(request, 'donnée.html')



def info_pollu(request):
    return render(request, 'info_pollu.html')




def machine_a_o(request):
    return render(request, 'machine a o.html')

def prediction(request):
    if request.method == "POST":
        
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
    
    return render(request, 'prediction.html')



def polution_lyon(request):


    a = heure()
    b = temps("lyon")
    c = particule("lyon")
    

    return render(request, 'polution_lyon.html', {'heure':a[0],'minute':a[1], 'temps':b, 'pollution':c})



def polution_marseille(request):

    a = heure()
    b = temps("marseille")
    c = particule("marseille")

    
    return render(request, 'polution_marseille.html', {'heure':a[0],'minute':a[1], 'temps':b, 'pollution':c})

def polution_paris(request):

    a = heure()
    b = temps("paris")
    c = particule("paris")
    
    return render(request, 'polution_paris.html', {'heure':a[0],'minute':a[1], 'temps':b, 'pollution':c})


def supp():
    
    pass

##    os.chdir('/app/static/popo')
##    liste = os.listdir()
##    for i in liste[1:-4]:
##        os.remove(i)
##    os.chdir('/app/polution')


def graphe(request):
    
    if request.method == "POST":
        
        ville = request.POST.get('ville')
        graphe = request.POST.get('graphe')
        

        print(ville, graphe)

        if graphe == 'bouchon':
            a = visu_bouchon(ville)
            donnée = traitement_bouchon(a)
            b = diagramme_bouchon(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], donnée[6], donnée[7], donnée[8], donnée[9],
                      donnée[10], donnée[11], 'diagramme.png')
            

            supp()
            return HttpResponse(b)


        elif graphe == 'climat':

            c = visuuu_climat(ville)
            donnée = traitementtt_climat(c)
            d = diagramme_climattt(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], donnée[6], donnée[7], donnée[8], donnée[9],
                      donnée[10], donnée[11], 'diagramme.png')
            supp()
            return HttpResponse(d)



        elif graphe == 'heure':
            horraire = traitement_heure(ville)
            e = diagramme_heure(horraire[0], horraire[1], horraire[2], horraire[3],
                            'diagramme.png')
            supp()
            return HttpResponse(e)




        
        elif graphe == 'manif':
            f = visu_manif(ville)
            donnée = traitement_manif(f)
            g = diagramme_manif(donnée[0], donnée[1],
                    donnée[2], donnée[3], 'diagramme.png')

            supp()
            return HttpResponse(g)




        elif graphe == 'météo':
            h = visu_climat(ville)
            donnée = traitement_climat(h)
            i = diagramme_climat(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], 'diagramme.png')
            
            supp()
            return HttpResponse(i)



                        
        elif graphe == 'population':
            j = visu_population()
            donnée = traitement_population(j)
            k = diagramme_population(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], 'diagramme.png')
            supp()
            return HttpResponse(k)

        
        elif graphe == 'pression':
            l = visu_pression(ville)
            donnée = traitement_pression(l)
            m = diagramme_pression(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], 'diagramme.png')

            supp()
            return HttpResponse(m)




    
        elif graphe == 'saison':
            n = visu_saison(ville)
            donnée = traitement_saison(n)

            o = diagramme_saison(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], donnée[6], donnée[7],
                             'diagramme.png')
            supp()
            return HttpResponse(o)


            
        elif graphe == 'vent':
            p = visu_vent(ville)
            donnée = traitement_vent(p)
            q = diagramme_vent(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
                      donnée[5], donnée[6], donnée[7],'diagramme.png')

            supp()
            return HttpResponse(q)

        
        elif graphe == 'weekend':

            r = visu_weekend(ville)
            donnée = traitement_weekend(r)
            s = diagramme_weekend(donnée[0], donnée[1], donnée[2], donnée[3],
                              'diagramme.png')
            supp()
            return HttpResponse(s)

        
        elif graphe == 'traffique':
            t = visu_traffique(ville)
            donnée = traitement_traffique(t)
            u = diagramme_traffique(donnée[0], donnée[1], donnée[2], donnée[3],
                                'diagramme.png')
            supp()
            return HttpResponse(u)
  

        
    return render(request, 'graphe.html')




def heure():

    date = datetime.datetime.now()

    heure = date.hour
    minute = date.minute

    return heure, minute





def temps(lieu):

    clé = '5a72ceae1feda40543d5844b2e04a205'
        
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)

    r = requests.get(localisation)

    data=r.json()
    
    méteo = data['weather'][0]['main']

    if méteo == "Clear":
        méteo = "Beau"

    elif méteo == "Clouds":
        méteo = "Nuageux"
    return méteo


def particule(lieu):


    path = "https://air.plumelabs.com/fr/live/{}".format(lieu)

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    liste = []
    propriete = soup.find_all("div")
    for i in propriete:
        liste.append(i.get_text())

    phrase_clé = "a atteint un niveau élevé de pollution. Supérieur à la limite maximum pour 24h établie par l'OMS"
    
    recherche_taux = str(liste).find(str(phrase_clé))
    liste_epluché = liste[20:21]
    polution = liste_epluché[0][31:34]

    return polution
    



















