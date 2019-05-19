from traitement import display_dict_particule
from traitement import display_dict
from traitement import raise_dict
from traitement import date_heure

from database import visualisation_table
from database import creation_conditions
from database import clean_data

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

liste = ['paris']

class data:


    def recuperation_data(self, city):
        self.city = city

        #météo
        météo.recuperation_donnée(self, city, WEATHER, WIND, PRESSURE) 
        données_météo = display_dict(PRESSURE, WEATHER, WIND)
        

        #climat
        climat.recuperation_donnée(self, city, CLIMAT)
        climat.saison(self, SAISON)
        données_climat = display_dict(CLIMAT, SAISON)


        #particule
        particule.france(self, city, VILLE_POLLUE2018)
        particule.industrie(self, city, REGION_INDUSTRIEL_POLLUEE)

        données_particule = display_dict(VILLE_POLLUE2018, REGION_INDUSTRIEL_POLLUEE)

        #socio
        socio.habitant(self, city, POPULATION_ACTIVE_HABITANT)
        données_socio = display_dict(POPULATION_ACTIVE_HABITANT)


        #traffique
        trafique.trafique_circulation(self, TRAFIQUE, HEURE)
        trafique.habitude(self, POINTE, WEEKEND)
        trafique.bouchons(self, city, BOUCHON)
        trafique.activité_execptionnelle(self, city, ACTIVITE_EXEPTIONNELLE)
        
        données_trafique =  display_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,
                     ACTIVITE_EXEPTIONNELLE)



        #particule
        particule.particule2(self,city, PARTICULE)
        données_parti = display_dict_particule(PARTICULE)


        return données_météo, données_climat, données_particule,\
            données_socio, données_trafique, données_parti

        
    def condition(self, données_météo, données_climat, données_particule,
                  données_socio, données_trafique, données_parti, city):


        données_actuelle = données_météo + données_climat + données_particule +\
                  données_socio + données_trafique



        
        THE_PARTICLE = []
        
        data = creation_conditions.visualisation_without_time(self, city)
        for i in data:
     
            i = list(i)
            if i == données_actuelle:

                
                particle = creation_conditions.recuperate_particle(self, city,
                                                                   i[0],i[1],i[2],i[3],
                                                                   i[4],i[5],i[6],i[7],
                                                                   i[8],i[9],i[10],i[11],
                                                                   i[12],i[13])

       
                THE_PARTICLE.append(particle)
                break


        print(THE_PARTICLE)
        if THE_PARTICLE == []:
            print('no donnée')

            
        else:
            c = 0
            var = 0
            for i in THE_PARTICLE[0]:
                i = int(i[0])
                var += i
                c+=1
            print(c)
            print("il y a a peu prés :", var/c, "AQI à", city)








        #raise 
        raise_dict(PARTICULE)
        raise_dict(TRAFIQUE, HEURE, POINTE, WEEKEND, BOUCHON,    
                    ACTIVITE_EXEPTIONNELLE)
        raise_dict(POPULATION_ACTIVE_HABITANT)
        raise_dict(VILLE_POLLUE2018, REGION_INDUSTRIEL_POLLUEE)
        raise_dict(CLIMAT, SAISON)
        raise_dict(PRESSURE, WEATHER, WIND)




if __name__ == '__main__':
    
    data = data()

    donnée = data.recuperation_data('paris')
    data.condition(donnée[0], donnée[1], donnée[2],
                   donnée[3], donnée[4], donnée[5], 'paris')
































