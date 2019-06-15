from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

from .prediction_site.analysa2 import *



def home(request):
    return render(request, 'home.html')


def polution(request):

    return render(request, 'polution.html')



def charger(request):
    return render(request, 'charger.html')

@csrf_exempt
def donnée(request):
    """Here we call API recup data, and display it on HTML page
    We need exception in case there are error from ur script (for call API)"""
    
    
    try:
        data_lyon = taux_particule('lyon')
        data_paris = taux_particule('paris')
        data_marseille = taux_particule('marseille')
    except:
        data_lyon = "No data"
        data_paris = "No data"
        data_marseille = "No data"  #First block particle data


        
    try:
        weather_lyon = temps_ville('lyon', 'météo')
        wind_lyon = temps_ville('lyon', 'vent')
        weather_paris = temps_ville('paris', 'météo')
        wind_paris = temps_ville('paris', 'vent')
        weather_marseille = temps_ville('marseille', 'météo')
        wind_marseille = temps_ville('marseille', 'vent')
        
    except:
        weather_lyon = "No data"
        wind_lyon = "No data"
        weather_paris = "No data"
        wind_paris = "No data"
        weather_marseille = "No data"
        wind_marseille = "No data"  #Second block Weather, Wind data


    try:
        temperature_lyon = climat_ville('lyon')
        temperature_paris = climat_ville('paris')
        temperature_marseille = climat_ville('marseille')
        current_season =  saison()
    except:
        temperature_lyon = "No data"
        temperature_paris = "No data"
        temperature_marseille = "No data"
        current_season = "No data"  #Third block Temperature,
                                    #Current season data


    try:
        traffic_lyon = traffique('lyon')
        departure_lyon = traffic_lyon[0] 
        hour_point_lyon = traffic_lyon[1]
        hour_point_paris = hour_point_lyon
        regular_day_lyon = traffic_lyon[2] 
        hour_point_marseille = hour_point_lyon

        if hour_point_marseille == 'oui':
            no_point_lyon = 'non'
            no_point_paris = 'non'
            no_point_marseille = 'non'
        else:
            no_point_lyon = 'oui'
            no_point_paris = 'oui'
            no_point_marseille = 'oui'

    except:
        traffic_lyon = "No data"
        departure_lyon = "No data"
        hour_point_lyon = "No data"
        hour_point_paris = "No data"
        regular_day_lyon = "No data"
        hour_point_marseille = "No data"    #Fourth block traffic
                                            #and Regular day data

    try:
        regular_day_paris = regular_day_lyon
        regular_day_marseille = regular_day_lyon
        departure_paris = departure_lyon
        departure_marseille = departure_lyon
        traffic_paris = traffique('paris')
        traffic_marseille = traffique('marseille')
        
    except:
        regular_day_paris = "No data"
        regular_day_marseille = "No data"
        departure_paris = "No data"
        traffic_paris = "No data"
        departure_marseille = "No data"
        traffic_paris = "No data"
        traffic_marseille = "No data"   #Fifty block regular day
                                        #Traffic and deaparture data


    try:
        day = habitude()
        weekend = ''
        if day == 'jour_semaine':
            day = 'semaine'
            weekend = 'non'
        else:
            day = 'week end'
            weekend = 'oui'
    except:
        day = "No data"     #Sixty bloc Day or Weekend data


    try:
        ranking_lyon = ville_pollué_classement('lyon')
        ranking_paris = ville_pollué_classement('paris')
        ranking_marseille = ville_pollué_classement('marseille')
        pole_lyon = region_industrielle('lyon')
        pole_paris = region_industrielle('paris')
        pole_marseille = region_industrielle('marseille')
        pressure_lyon = pression_ville('lyon')
        pression_paris = pression_ville('paris')
        pression_marseille = pression_ville('marseille')
        demonstration_lyon = activité_execptionnelle('lyon')
        demonstration_paris = activité_execptionnelle('paris')
        demonstration_marseille = activité_execptionnelle('marseille')
        
    except:
        ranking_lyon = "No data"
        ranking_paris = "No data"
        ranking_marseille = "No data"
        pole_lyon = "No data"
        pole_paris = "No data"
        pole_marseille = "No data"
        pressure_lyon = "No data"
        pression_paris = "No data"
        pression_marseille = "No data"
        demonstration_lyon = "No data"
        demonstration_paris = "No data"
        demonstration_marseille = "No data"
                                #Seve,ty bloc Ranking data, Pole and
                                #Demonstration data
    try:
        socio_lyon = socio('lyon')
        socio_paris = socio('paris')
        socio_marseille = socio('marseille')
        plugs_lyon = bouchons('lyon')
        plugs_paris = bouchons('paris')


        errup = eruption()
        if errup == 'oui':
            pass
        else:
            errup = 'non'
        
        diesel = recup_balise()
        dollars = cours_dollar()

    except:
        socio_lyon = "No data"
        socio_paris = "No data"
        socio_marseille = "No data"
        plugs_lyon = "No data"
        plugs_paris = "No data"
        errup = "No data"
        diesel = "No data"
        dollars = "No data" #Heighty block Socio, Plugs, Diesel
                            #Dollars and Eruption data

    try:
        fire_lyon = incendie('lyon')
        
        if fire_lyon == 'oui':
            fire_lyon = 'oui'
        else:
            fire_lyon = 'non'
        
        fire_marseille = incendie('marseille')
        
        if fire_marseille == 'oui':
            fire_marseille = 'oui'
        else:
            fire_marseille = 'non'
            
        fire_paris = incendie('paris')
        if fire_paris == 'oui':
            fire_paris = 'oui'
        else:
            fire_paris = 'non'


        fertilizer = periode_angrais()
        periode = nuit_jour()
        po_lyon = polenne('lyon')
        po_marseille = polenne('marseille')
        po_paris = polenne('paris')

    except:
        fire_lyon = "No data"
        fire_marseille = "No data"
        fire_paris = "No data"
        fertilizer = "No data"
        periode = "No data"
        po_lyon = "No data"
        po_marseille = "No data"
        po_paris = "No data"
                    #Ninety bloc Fire, Periode, And Po data


    return render(request, 'donnée.html', {'lyon':data_lyon,
                                           'paris':data_paris,
                                           'marseille':data_marseille,
                                           'weather_lyon':weather_lyon,
                                           'weather_marseille':weather_marseille,
                                           'weather_paris':weather_paris,
                                           'wind_lyon':wind_lyon,
                                           'wind_paris':wind_paris,
                                           'wind_marseille':wind_marseille,
                                           'temperature_lyon':round(temperature_lyon),
                                           'temperature_paris':round(temperature_paris),
                                           'temperature_marseille':round(temperature_marseille),
                                           'current_season':current_season,
                                           'departure_lyon':departure_lyon,
                                           'hour_point_lyon':hour_point_lyon,
                                           'regular_day_lyon':regular_day_lyon,
                                           'no_point_lyon':no_point_lyon,
                                           'departure_paris':departure_paris,
                                           'hour_point_paris':hour_point_paris,
                                           'regular_day_marseille':regular_day_marseille,
                                           'no_point_marseille':no_point_marseille,
                                           'departure_paris':departure_paris,
                                           'hour_point_paris':hour_point_paris,
                                           'regular_day_paris':regular_day_paris,
                                           'no_point_paris':no_point_paris,
                                           'weekend':weekend,
                                           'week_day':day,
                                           'ranking_lyon':ranking_lyon,
                                           'ranking_paris':ranking_paris,
                                           'ranking_marseille':ranking_marseille,
                                           'pole_lyon':pole_lyon,
                                           'pole_paris':pole_paris,
                                           'pole_marseille':pole_marseille,
                                           'pressure_lyon':pressure_lyon,
                                           'pressure_paris':pression_paris,
                                           'pressure_marseille':pression_marseille,
                                           'demonstration_lyon':demonstration_lyon,
                                           'demonstration_paris':demonstration_paris,
                                           'demonstration_marseille':demonstration_marseille,
                                           'socio_lyon':socio_lyon,
                                           'socio_marseille':socio_marseille,
                                           'socio_paris':socio_paris,
                                           'plugs_lyon':plugs_lyon,
                                           'plugs_paris':plugs_paris,
                                           'eruption':errup,
                                           'diesel':diesel,
                                           'dollars':dollars,
                                           'fire_lyon':fire_lyon,
                                           'fire_marseille':fire_marseille,
                                           'fire_paris':fire_paris,
                                           'fertilizer':fertilizer,
                                           'periode':periode,
                                           'po_lyon':po_lyon,
                                           'po_paris':po_paris,
                                           'po_marseille':po_marseille})

                        #Return it !





def info_pollu(request):
    """Information page about pollution"""
    return render(request, 'info_pollu.html')




def machine_a_o(request):
    """Information page about Water machin"""
    
    return render(request, 'machine a o.html')

@csrf_exempt
def prediction(request):
    """Our predict page"""
    if request.method == "POST":

            ville1 = request.POST.get('lyon')
            ville2 = request.POST.get('paris')
            ville3 = request.POST.get('marseille')

            if ville1:
                predi = predi_analysa2('lyon')
                return HttpResponse(predi)

            if ville2:
                predi = predi_analysa2('paris')
                return HttpResponse(predi)

            if ville3:
                predi = predi_analysa2('marseille')
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



@csrf_exempt
def graphe(request):
    """Graphic page"""
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
    



















