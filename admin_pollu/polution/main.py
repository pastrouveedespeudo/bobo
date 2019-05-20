import importlib
import datetime

from socio import habitant

from trafique import trafique_circulation
from trafique import habitude
from trafique import bouchons
from trafique import requete_lyon_traffique
from trafique import requete_paris_traffique
from trafique import requete_marseille_traffique
from trafique import activité_execptionnelle

from particule import particule
from particule import particule2
from particule import france
from particule import industrie

from particule import france
from particule import industrie

from variable import WEATHER
from variable import WIND
from variable import PRESSURE
from variable import SAISON
from variable import CLIMAT
from variable import REGION_INDUSTRIEL_POLLUEE
from variable import PARTICULE
from variable import VILLE_POLLUE2018
from variable import REGION_INDUSTRIEL_POLLUEE
from variable import POPULATION_ACTIVE_HABITANT
from variable import TRAFIQUE
from variable import HEURE
from variable import POINTE
from variable import WEEKEND
from variable import BOUCHON
from variable import ACTIVITE_EXEPTIONNELLE
from variable import PARTICULE_PLAGE

from variable import LIST_CITY

from traitement import display_dict_particule
from traitement import display_dict
from traitement import raise_dict
from traitement import date_heure

from météo import recuperation_donnée_météo

from climat import recuperation_donnée_température
from climat import saison


from database2 import insertion_meteo
from database2 import insertion_climat
from database2 import insertion_polution
from database2 import insertion_sociologie
from database2 import insertion_trafic_routier
from database2 import insertion_particule_plage
from database2 import insertion_particule





def météologie():

    referentiel = date_heure()

    
    for i in LIST_CITY:
        print(i)

        recuperation_donnée_météo(i, WEATHER, WIND, PRESSURE)
        
        données = display_dict(PRESSURE, WEATHER, WIND)
        print(données)
        insertion_meteo(i, referentiel[0],
                        referentiel[1],
                        données[0], données[1],
                        données[2])

        raise_dict(PRESSURE, WEATHER, WIND)
        

def climat():

    referentiel = date_heure()

    
    for i in LIST_CITY:
        print(i)

        recuperation_donnée_température(i, CLIMAT)
        saison(SAISON)
        
        données = display_dict(CLIMAT, SAISON)
        print(données)
        insertion_climat(données[0], données[1],
                        referentiel[0],referentiel[1], i)
        
        raise_dict(CLIMAT, SAISON)   


def pollution():

    referentiel = date_heure()

    for i in LIST_CITY:
        print(i)
        
        france(i, VILLE_POLLUE2018)
        industrie(i, REGION_INDUSTRIEL_POLLUEE)

        données = display_dict(VILLE_POLLUE2018,
                     REGION_INDUSTRIEL_POLLUEE)
        print(données)
        insertion_polution(données[0], données[1],
                          referentiel[0],referentiel[1], i)
        
        raise_dict(VILLE_POLLUE2018,
                   REGION_INDUSTRIEL_POLLUEE)



def sociologie():

    referentiel = date_heure()

    
    for i in LIST_CITY:
        print(i)
        
        habitant(i, POPULATION_ACTIVE_HABITANT)
    
        données = display_dict(POPULATION_ACTIVE_HABITANT)
        print(données)
        insertion_sociologie(données[0], referentiel[0],
                            referentiel[1], i)
         
        raise_dict(POPULATION_ACTIVE_HABITANT)




def trafic_routier():

    referentiel = date_heure()

    for i in LIST_CITY:
        print(i)

        trafique_circulation(TRAFIQUE, HEURE)
        habitude(POINTE, WEEKEND)
        bouchons(i, BOUCHON)
        activité_execptionnelle(i, ACTIVITE_EXEPTIONNELLE)
        
        données =  display_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,
                     ACTIVITE_EXEPTIONNELLE)
        print(données)


        insertion_trafic_routier(données[0], données[1],
                                données[2], données[3], données[4], données[5],
                                referentiel[0], referentiel[1], i)

                    
        raise_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,
                   ACTIVITE_EXEPTIONNELLE)


def particule_plage():

    referentiel = date_heure()

    print('\n')
    for i in LIST_CITY:
        print(i) 

        particule(i, PARTICULE_PLAGE)
        
        données = display_dict(PARTICULE_PLAGE)
        print(données)
        insertion_particule_plage(données[0], referentiel[0],#ICI#ICI
                                 referentiel[1], i)
        
        raise_dict(PARTICULE_PLAGE)


def particulee():

    referentiel = date_heure()

    print('\n')
    for i in LIST_CITY:
        print(i) 

        particule2(i, PARTICULE)
        
        données = display_dict_particule(PARTICULE)
        print(données)
        insertion_particule(données[0], referentiel[0],#ICI#ICI
                            referentiel[1], i)
        
        raise_dict(PARTICULE)

        



météologie()
climat()       
pollution()
sociologie()
trafic_routier()
particulee()
particule_plage()












