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


from .prediction_site.analysa2 import *

from .views_function import data_function_particle
from .views_function import data_function_weather
from .views_function import data_function_wind
from .views_function import data_function_temperature
from .views_function import data_function_season
from .views_function import data_function_departure
from .views_function import data_function_day
from .views_function import data_function_ranking
from .views_function import data_function_pole
from .views_function import data_function_pressure
from .views_function import data_function_demonstration
from .views_function import function_data_socio
from .views_function import function_data_plugs
from .views_function import function_data_erup
from .views_function import function_data_dollars
from .views_function import function_data_fire
from .views_function import function_data_ferti
from .views_function import function_data_periode


def home(request):
    """Here we return html home response"""
    return render(request, 'home.html')

def navebarre_donnee(request):
    """Here we return html home response"""
    return render(request, 'navebarre_donnee.html')

def navebarre_graphe(request):
    """Here we return html home response"""
    return render(request, 'navebarre_graphe.html')

def navebarre_info(request):
    """Here we return html home response"""
    return render(request, 'navebarre_info.html')

def navebarre_prediction(request):
    """Here we return html home response"""
    return render(request, 'navebarre_prediction.html')


def navebarre_vent(request):
    """Here we return html home response"""
    return render(request, 'navebarre_vent.html')

def navebarre_soluce(request):
    """Here we return html home response"""
    return render(request, 'navebarre_soluce.html')


def polution(request):
    """we return html pollution response"""
    return render(request, 'polution.html')



def donnée(request):
    """Here we call all API recup data, and display it on HTML page
    We need exception in case there are error from ur script (for call API)"""
    
    particle =  data_function_particle()
    weather = data_function_weather()
    wind = data_function_wind()
    temperature = data_function_temperature()
    season = data_function_season()
    deaparture = data_function_departure()
    day = data_function_day()
    rank = data_function_ranking()
    pressure = data_function_pressure()
    demonstration = data_function_demonstration()
    socio = function_data_socio()
    plugs = function_data_plugs()
    erup = function_data_erup()
    dollars = function_data_dollars()
    fire = function_data_fire()
    fertilizer = function_data_ferti()
    periode = function_data_periode()
    pole = data_function_pole()


    
    return render(request, 'donnée.html', {'lyon':particle[0],
                                           'paris':particle[1],
                                           'marseille':particle[2],
                                           'weather_lyon':weather[0],
                                           'weather_marseille':weather[1],
                                           'weather_paris':weather[2],
                                           'wind_lyon':wind[0],
                                           'wind_paris':wind[1],
                                           'wind_marseille':wind[2],
                                           'temperature_lyon':round(temperature[0]),
                                           'temperature_paris':round(temperature[1]),
                                           'temperature_marseille':round(temperature[2]),
                                           'current_season':season,
                                           'departure_lyon':deaparture[0],
                                           'hour_point_lyon':deaparture[1],
                                           'regular_day_lyon':deaparture[2],
                                           'no_point_lyon':deaparture[3],
                                           'departure_marseille':deaparture[0],
                                           'hour_point_paris':deaparture[1],
                                           'regular_day_marseille':deaparture[2],
                                           'no_point_marseille':deaparture[3],
                                           'departure_paris':deaparture[0],
                                           'hour_point_marseille':deaparture[1],
                                           'regular_day_paris':deaparture[2],
                                           'no_point_paris':deaparture[3],
                                           'weekend':day[0],
                                           'week_day':day[1],
                                           'ranking_lyon':rank[0],
                                           'ranking_paris':rank[1],
                                           'ranking_marseille':rank[2],
                                           'pole_lyon':pole[0],
                                           'pole_paris':pole[1],
                                           'pole_marseille':pole[2],
                                           'pressure_lyon':pressure[0],
                                           'pressure_paris':pressure[1],
                                           'pressure_marseille':pressure[2],
                                           'demonstration_lyon':demonstration[0],
                                           'demonstration_paris':demonstration[1],
                                           'demonstration_marseille':demonstration[2],
                                           'socio_lyon':socio[0],
                                           'socio_marseille':socio[2],
                                           'socio_paris':socio[1],
                                           'plugs_lyon':plugs[0],
                                           'plugs_paris':plugs[1],
                                           'eruption':erup,
                                           'diesel':dollars[0],
                                           'dollars':dollars[1],
                                           'fire_lyon':fire[0],
                                           'fire_marseille':fire[1],
                                           'fire_paris':fire[2],
                                           'fertilizer':fertilizer,
                                           'periode':periode[0],
                                           'po_lyon':periode[1],
                                           'po_paris':periode[2],
                                           'po_marseille':periode[3]})

                        
    return render(request, 'donnée.html')


def info_pollu(request):
    """Information page about pollution"""
    return render(request, 'info_pollu.html')


def machine_a_o(request):
    """Information page about Water machin"""
    
    return render(request, 'machine_a_o.html')


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
                #from predi_site.analysa2.py
                predi = predi_analysa2('lyon')
                return HttpResponse(predi)

            if city2:
                predi = predi_analysa2('paris')
                return HttpResponse(predi)

            if city3:
                predi = predi_analysa2('marseille')
                return HttpResponse(predi)
                
    return render(request, 'prediction.html')





def graphe(request):
    """Graphic page. Here we ask database by Ajax call
    for each conditions by function who begin
    by visu, traiting this data with function who begin by traitement,
    we make an average and a variance by fonction_graphe from graphe file
    and display it by graphe function with matplotlib"""

    #Ajax call
    if request.method == "POST":
        
        #We recup city
        #And the condition
        #For example Lyon condition plugs
        city = request.POST.get('city')    
        graph = request.POST.get('graph')  
                                            
        print(city, graph)

        #We ask database
        #We trait it
        if graph == 'plugs':
            a = visu_plugs(city)       
            data = treatment_plugs(a)
            #and make a visual by matplolib
            b = diagram_plugs(data[0], data[1], data[2], data[3], data[4],
                      data[5], data[6], data[7], data[8], data[9],
                      data[10], data[11], 'diagramme.png')  
        
            #and return a HttpResponse, here the graph
            return HttpResponse(b)



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
    """We recup weather from api openweathermap"""
    
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
    """particle stuff we recup particle from airplumair"""

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
    



















