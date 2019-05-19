import importlib
import datetime

from socio import socio
from trafique import trafique
from météo import météo
from particule import particule
from climat import climat

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

from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE

from database import insertion_table
from database import visualisation_table


class main:

    
    def météologie(self):

        referentiel = date_heure()

        
        for i in LIST_CITY:
            print(i)

            météo.recuperation_donnée(self, i, WEATHER, WIND, PRESSURE)
            
            données = display_dict(PRESSURE, WEATHER, WIND)
            print(données)
            insertion_table.insertion_meteo(self, i, referentiel[0],
                                            referentiel[1],
                                            données[0], données[1],
                                            données[2])

            raise_dict(PRESSURE, WEATHER, WIND)
            

    def climat(self):

        referentiel = date_heure()
    
        
        for i in LIST_CITY:
            print(i)

            climat.recuperation_donnée(self, i, CLIMAT)
            climat.saison(self, SAISON)
            
            données = display_dict(CLIMAT, SAISON)
            
            insertion_table.insertion_climat(self, données[0], données[1],
                                             referentiel[0],referentiel[1], i)
            
            raise_dict(CLIMAT, SAISON)   


    def pollution(self):

        referentiel = date_heure()

        for i in LIST_CITY:
            print(i)
            
            particule.france(self, i, VILLE_POLLUE2018)
            particule.industrie(self, i, REGION_INDUSTRIEL_POLLUEE)

            données = display_dict(VILLE_POLLUE2018,
                         REGION_INDUSTRIEL_POLLUEE)

            insertion_table.insertion_polution(self, données[0], données[1],
                                               referentiel[0],referentiel[1], i)
            
            raise_dict(VILLE_POLLUE2018,
                       REGION_INDUSTRIEL_POLLUEE)


    def sociologie(self):

        referentiel = date_heure()

        
        for i in LIST_CITY:
            print(i)
            
            socio.habitant(self, i, POPULATION_ACTIVE_HABITANT)
        
            données = display_dict(POPULATION_ACTIVE_HABITANT)

            insertion_table.insertion_sociologie(self, données[0], referentiel[0],
                                                referentiel[1], i)
             
            raise_dict(POPULATION_ACTIVE_HABITANT)


    def trafic_routier(self):

        referentiel = date_heure()

        for i in LIST_CITY:
            print(i)

            trafique.trafique_circulation(self, TRAFIQUE, HEURE)
            trafique.habitude(self, POINTE, WEEKEND)
            trafique.bouchons(self, i, BOUCHON)
            trafique.activité_execptionnelle(self, i, ACTIVITE_EXEPTIONNELLE)
            
            données =  display_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,
                         ACTIVITE_EXEPTIONNELLE)
            print(données)


            insertion_table.insertion_trafic_routier(self, données[0], données[1],
                                                     données[2], données[3], données[4], données[5],
                                                     referentiel[0], referentiel[1], i)

                        
            raise_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,
                       ACTIVITE_EXEPTIONNELLE)


    def particule_plage(self):

        referentiel = date_heure()

        print('\n')
        for i in LIST_CITY:
            print(i) 

            particule.particule(self,i, PARTICULE_PLAGE)
            
            données = display_dict(PARTICULE_PLAGE)

            insertion_table.insertion_particule_plage(self, données[0], referentiel[0],
                                                referentiel[1], i)
            
            raise_dict(PARTICULE_PLAGE)


    def particule(self):

        referentiel = date_heure()

        print('\n')
        for i in LIST_CITY:
            print(i) 

            particule.particule2(self,i, PARTICULE)
            
            données = display_dict_particule(PARTICULE)

            insertion_table.insertion_particule(self, données[0], referentiel[0],
                                                referentiel[1], i)
            
            raise_dict(PARTICULE)

            

if __name__ == '__main__':

    main = main()
    main.météologie()
    main.climat()
    main.pollution()
    main.sociologie()
    main.trafic_routier()
    main.particule()
    main.particule_plage()












