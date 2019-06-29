from direction.ville import ville
from direction.nouvel_pos import long_lat
from direction.boussole import calcul_vent
from direction.vent import *

from direction.superficie import *
from direction.addresse import *


if __name__=="__main__": 
  


    def runner(liste):

        new_lat = ''
        new_long = ''

        while True:

            for i in liste:
                
                if new_lat != '' and new_long != '':

                    adresse = dress_to_ville(new_lat, new_long)
                    position_vent = vent_deux(adresse[0])
                    vent = superficie_ville(adresse[1])
                    print(vent)

                else:
             
                    lat, long = ville(i)
                    adresse = dress_to_ville(lat, long)
                    position_vent = vent_deux(i)
                    vent = superficie_ville(adresse[1])
                    print(vent)


                if new_lat != '' and new_long != '':
                    
                    nouvelle_position = long_lat(new_lat, new_long, vent, position_vent)
                    
                else:
                          
                    nouvelle_position = long_lat(lat, long, vent, position_vent)  
                
                new_lat = nouvelle_position[0]
                new_long = nouvelle_position[1]

                
