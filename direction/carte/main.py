
from direction.ville import ville
from direction.nouvel_pos import long_lat
from direction.boussole import calcul_vent
from direction.vent import le_vent

from direction.superficie import *
from direction.addresse import *


if __name__=="__main__": 
    liste = ['Ruy']


    new_lat = ''
    new_long = ''


    while True:

        for i in liste:
            
            if new_lat != '' and new_long != '':
                
                print('de lattitude:', new_lat, 'et de longitude', new_long)
                
                adresse = dress_to_ville(new_lat, new_long)
      
                print('adresse trouvée :', adresse)
                
                a, degres_vent = le_vent(adresse)
                try:
                    vent = superficie_ville(adresse)
                    print(vent,'2')
                except:
                    vent = vent_deux(adresse)
                    print(vent)

                
            else:
                
                lat, long = ville(i)
                
                adresse = dress_to_ville(lat, long)
                
                print('de lattitude:', lat, 'de longitude', long)
                
                a, degres_vent = le_vent(i)
                try:
                    vent = superficie_ville(adresse)
                    print(vent,'1')
                except:
                    vent = vent_deux(adresse)
                    print(vent)

            
            #print('vent de :', vent, 'de degres :', degres_vent, '\n')
                
            position_vent = calcul_vent(degres_vent)
            print('donc le vent va vers:', position_vent)

            

            
            if new_lat != '' and new_long != '':
                
                nouvelle_position = long_lat(new_lat, new_long, vent, position_vent)
                print('la nouvelle position est de :', nouvelle_position)
                
            else:
                      
                nouvelle_position = long_lat(lat, long, vent, position_vent)
                print('la nouvelle position est de :', nouvelle_position)    
            
            new_lat = nouvelle_position[0]
            new_long = nouvelle_position[1]

            
            print('\n')


            

















