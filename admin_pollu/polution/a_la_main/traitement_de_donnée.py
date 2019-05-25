from .socio import habitant

from .trafique import trafique_circulation
from .trafique import habitude
from .trafique import bouchons
from .trafique import requete_lyon_traffique
from .trafique import requete_paris_traffique
from .trafique import requete_marseille_traffique
from .trafique import activité_execptionnelle

from .particule import particule
from .particule import particule2
from .particule import france
from .particule import industrie

from .particule import france
from .particule import industrie

from .variable import WEATHER
from .variable import WIND
from .variable import PRESSURE
from .variable import SAISON
from .variable import CLIMAT
from .variable import REGION_INDUSTRIEL_POLLUEE
from .variable import PARTICULE
from .variable import VILLE_POLLUE2018
from .variable import REGION_INDUSTRIEL_POLLUEE
from .variable import POPULATION_ACTIVE_HABITANT
from .variable import TRAFIQUE
from .variable import HEURE
from .variable import POINTE
from .variable import WEEKEND
from .variable import BOUCHON
from .variable import ACTIVITE_EXEPTIONNELLE
from .variable import PARTICULE_PLAGE

from .traitement import display_dict_particule
from .traitement import display_dict
from .traitement import raise_dict
from .traitement import date_heure

from .météo import recuperation_donnée_météo

from .climat import recuperation_donnée_température
from .climat import saison

from .database2 import visualisation_without_time
from .database2 import recuperate_particle



def recuperation_data(city):


    #météo
    recuperation_donnée_météo(city, WEATHER, WIND, PRESSURE) 
    données_météo = display_dict(PRESSURE, WEATHER, WIND)
    

    #climat
    recuperation_donnée_température(city, CLIMAT)
    saison(SAISON)
    données_climat = display_dict(CLIMAT, SAISON)


    #particule
    france(city, VILLE_POLLUE2018)
    industrie(city, REGION_INDUSTRIEL_POLLUEE)

    données_particule = display_dict(VILLE_POLLUE2018, REGION_INDUSTRIEL_POLLUEE)

    #socio
    habitant(city, POPULATION_ACTIVE_HABITANT)
    données_socio = display_dict(POPULATION_ACTIVE_HABITANT)


    #traffique
    trafique_circulation(TRAFIQUE, HEURE)
    habitude(WEEKEND)
    bouchons(city, BOUCHON)
    activité_execptionnelle(city, ACTIVITE_EXEPTIONNELLE)
    
    données_trafique =  display_dict(TRAFIQUE, HEURE, WEEKEND, BOUCHON,
                 ACTIVITE_EXEPTIONNELLE)



    #particule
    particule2(city, PARTICULE)
    données_parti = display_dict_particule(PARTICULE)


    return données_météo, données_climat, données_particule,\
        données_socio, données_trafique, données_parti

    
def condition(données_météo, données_climat, données_particule,
              données_socio, données_trafique, données_parti, city):


    donnée = ''

    données_actuelle = données_météo + données_climat + données_particule +\
              données_socio + données_trafique



    
    THE_PARTICLE = []
    
    data = visualisation_without_time(city)
    for i in data:
 
        i = list(i)
        if i == données_actuelle:

            
            particle = recuperate_particle(city,
                                           i[0],i[1],i[2],i[3],
                                           i[4],i[5],i[6],i[7],
                                           i[8],i[9],i[10],i[11],
                                           i[12])

   
            THE_PARTICLE.append(particle)
            break


    print(THE_PARTICLE)
    if THE_PARTICLE == []:
        print('no donnée')
        donnée = 'no donnée'

        
    else:
        c = 0
        var = 0
        for i in THE_PARTICLE[0]:
            i = int(i[0])
            var += i
            c+=1
        print(c)
        print("il y a a peu prés :", var/c, "AQI à", city)
        donnée = var/c







    #raise 
    raise_dict(PARTICULE)
    raise_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,    
                ACTIVITE_EXEPTIONNELLE)
    raise_dict(POPULATION_ACTIVE_HABITANT)
    raise_dict(VILLE_POLLUE2018, REGION_INDUSTRIEL_POLLUEE)
    raise_dict(CLIMAT, SAISON)
    raise_dict(PRESSURE, WEATHER, WIND)


    return donnée






































