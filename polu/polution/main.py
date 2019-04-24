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
            
            displaying = display_dict(PRESSURE, WEATHER, WIND)
            
            raise_dict(PRESSURE, WEATHER, WIND)

            print('\n')

    def pollution(self):
        
        particule.particule(self,'paris', PARTICULE)
        particule.france(self, 'paris', VILLE_POLLUE2018)
        particule.industrie(self, 'paris', REGION_INDUSTRIEL_POLLUEE)

        print(PARTICULE)
        print(VILLE_POLLUE2018)
        print(REGION_INDUSTRIEL_POLLUEE)


    def sociologie(self):
        
        socio.habitant(self, 'paris', POPULATION_ACTIVE_HABITANT)
        
        print(POPULATION_ACTIVE_HABITANT)



    def trafic_routier(self):
        
        trafique.trafique_circulation(self, TRAFIQUE, HEURE)
        trafique.habitude(self, POINTE, WEEKEND)
        trafique.bouchons(self, 'paris', BOUCHON)
        trafique.activité_execptionnelle(self, 'paris', ACTIVITE_EXEPTIONNELLE)

        print(TRAFIQUE)
        print(HEURE)
        print(POINTE)
        print(WEEKEND)
        print(BOUCHON)
        print(ACTIVITE_EXEPTIONNELLE)







if __name__ == '__main__':

    main = main()
    main.météologie()
    #main.pollution()
    #main.sociologie()
    #main.trafic_routier()












