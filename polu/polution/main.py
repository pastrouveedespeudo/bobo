import importlib

from socio import socio
from trafique import trafique
from météo import météo
from particule import particule
from climat import climat

from variable import WEATHER
from variable import WIND
from variable import PRESSURE
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

from variable import LIST_CITY

from traitement import display_dict
from traitement import raise_dict

class main:

    def météologie(self):
        
        for i in LIST_CITY:
            print(i)

            météo.recuperation_donnée(self, i, WEATHER,WIND,PRESSURE)
            
            display_dict(PRESSURE, WEATHER, WIND)
            raise_dict(PRESSURE, WEATHER, WIND)

            

    def pollution(self):

        for i in LIST_CITY:
            print(i)
            
            particule.particule(self,i, PARTICULE)
            particule.france(self, i, VILLE_POLLUE2018)
            particule.industrie(self, i, REGION_INDUSTRIEL_POLLUEE)

            display_dict(PARTICULE, VILLE_POLLUE2018,
                         REGION_INDUSTRIEL_POLLUEE)
            
            raise_dict(PARTICULE, VILLE_POLLUE2018,
                       REGION_INDUSTRIEL_POLLUEE)


    def sociologie(self):
        
        for i in LIST_CITY:
            print(i)
            
            socio.habitant(self, i, POPULATION_ACTIVE_HABITANT)
        
            display_dict(POPULATION_ACTIVE_HABITANT)
            raise_dict(POPULATION_ACTIVE_HABITANT)


    def trafic_routier(self):

        for i in LIST_CITY:
            print(i)

            
            trafique.trafique_circulation(self, TRAFIQUE, HEURE)
            trafique.habitude(self, POINTE, WEEKEND)
            trafique.bouchons(self, i, BOUCHON)
            trafique.activité_execptionnelle(self, i, ACTIVITE_EXEPTIONNELLE)
            
            display_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE)
            raise_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE)








if __name__ == '__main__':

    main = main()
    #main.météologie()
    #main.pollution()
    #main.sociologie()
    main.trafic_routier()












