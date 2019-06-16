from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import requests
import urllib.request
import datetime
from bs4 import *

from .graph.graphic_plugs import *
from .graph.graphic_climate import *
from .graph.graphic_hour import *
from .graph.graphic_demonstration import *
from .graph.graphic_weather import *
from .graph.graphic_pressure import *
from .graph.graphic_season import *
from .graph.graphic_traffic import *
from .graph.graphic_wind import *
from .graph.graphic_weekend import *
from .graph.graphic_population import *

from.polu_ana.polution.traitement_de_donnée import recuperation_data
from.polu_ana.polution.traitement_de_donnée import condition

from .polu_ana.polution.database2 import *
from .donnée_site.pollution import *

from .data_site.angrais import *
from .data_site.diesel import *
from .data_site.eruption import *
from .data_site.incendie import *
from .data_site.jour_nuit import *
from .data_site.polenne import *

from .prediction_site.analysa2 import *



def home(request):
    """Here we return html home response"""
    return render(request, 'home.html')


def polution(request):
    """we return html pollution response"""
    return render(request, 'polution.html')




@csrf_exempt
def donnée(request):
    """Here we call all API recup data, and display it on HTML page
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
                    #Ninth bloc Fire, Periode, And Po data


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
    """Our predict page. By Ajax call
    We recup this cities and ask database by aide_analysa.py
    from prediction_site and try to match by condition
    with analysa2.py and return it in html page"""

    
    if request.method == "POST":
                                
            city1 = request.POST.get('lyon')    
            city2 = request.POST.get('paris')
            city3 = request.POST.get('marseille')

            if city1:
                predi = predi_analysa2('lyon')#from predi_site.analysa2.py
                return HttpResponse(predi)

            if city2:
                predi = predi_analysa2('paris')
                return HttpResponse(predi)

            if city3:
                predi = predi_analysa2('marseille')
                return HttpResponse(predi)
                
    return render(request, 'prediction.html')




@csrf_exempt
def graphe(request):
    """Graphic page. Here we ask database by Ajax call
    for each conditions by function who begin
    by visu, traiting this data with function who begin by traitement,
    we make an average and a variance by fonction_graphe from graphe file
    and display it by graphe function with matplotlib"""

    
    if request.method == "POST": #Ajax call
            
        city = request.POST.get('city')    #We recup city
        graph = request.POST.get('graph')  #And the condition
                                            #For example Lyon condition plugs
        

        print(city, graph)

        if graph == 'plugs':
            a = visu_plugs(city)       #We ask database
            data = treatment_plugs(a)  #We trait it
            b = diagram_plugs(data[0], data[1], data[2], data[3], data[4],
                      data[5], data[6], data[7], data[8], data[9],
                      data[10], data[11], 'diagramme.png')  #and make a visual by matplolib
        
           
            return HttpResponse(b)#and return a HttpResponse, here the graph



        elif graph == 'hour':
            schedule = treatment_hour(city)
            e = diagram_hour(schedule[0], schedule[1], schedule[2], schedule[3],
                            'diagramme.png')
       
            return HttpResponse(e)



        elif graph == 'demonstration':
            f = visu_demonstration(city)
            data = treatement_demonstration(f)
            g = diagram_demonstration(data[0], data[1],
                    data[2], data[3], 'diagramme.png')

            
            return HttpResponse(g)




        elif graph == 'weather':
            h = visu_weater(city)
            data = treatement_weather(h)
            i = diagram_weather(data[0], data[1], data[2], data[3], data[4],
                      data[5], 'diagramme.png')
            
           
            return HttpResponse(i)



                        
        elif graph == 'population':
            j = visu_population()
            data = treatement_population(j)
            k = diagram_population(data[0], data[1], data[2], data[3], data[4],
                      data[5], 'diagramme.png')
           
            return HttpResponse(k)

        
        elif graph == 'pressure':
            l = visu_pressure(city)
            data = treatment_pressure(l)
            m = diagram_pressure(data[0], data[1], data[2], data[3], data[4],
                      data[5], 'diagramme.png')

         
            return HttpResponse(m)




    
        elif graph == 'season':
            n = visu_season(city)
            data = treatment_season(n)

            o = diagram_season(data[0], data[1], data[2], data[3], data[4],
                      data[5], data[6], data[7],
                             'diagramme.png')
        
            return HttpResponse(o)


            
        elif graph == 'wind':
            p = visu_wind(city)
            data = treatment_wind(p)
            q = diagram_wind(data[0], data[1], data[2], data[3], data[4],
                      data[5], data[6], data[7],'diagramme.png')

            
            return HttpResponse(q)

        
        elif graph == 'weekend':

            r = visu_weekend(city)
            data = treatment_weekend(r)
            s = diagram_weekend(data[0], data[1], data[2], data[3],
                              'diagramme.png')
         
            return HttpResponse(s)

        
        elif graph == 'traffic':
            t = visu_traffic(city)
            data = treatment_traffic(t)
            u = diagram_traffic(data[0], data[1], data[2], data[3],
                                'diagramme.png')
   
            return HttpResponse(u)
  

        
    return render(request, 'graphe.html')




def hour():

    date = datetime.datetime.now()

    hours = date.hour
    minute = date.minute

    return hours, minute





def temps(lieu):

    clé = '5a72ceae1feda40543d5844b2e04a205'
        
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)

    r = requests.get(localisation)

    data=r.json()
    
    weather = data['weather'][0]['main']

    if weather == "Clear":
        weather = "Beau"

    elif weather == "Clouds":
        weather = "Nuageux"
    return weather


def particle(lieu):


    path = "https://air.plumelabs.com/fr/live/{}".format(lieu)

    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    liste = []
    propriete = soup.find_all("div")
    for i in propriete:
        liste.append(i.get_text())

    sentence = "a atteint un niveau élevé de pollution. Supérieur à la limite maximum pour 24h établie par l'OMS"
    
    search = str(liste).find(str(sentence))
    liste_e = liste[20:21]
    pollute = liste_e[0][31:34]

    return pollute
    



















