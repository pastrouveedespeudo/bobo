
from direction.ville import ville
from direction.addresse import par_lat_par_long
from direction.nouvel_pos import long_lat
from direction.boussole import calcul_vent
from direction.vent import le_vent


liste = ['crest']


new_lat = ''
new_long = ''





while True:

    for i in liste:
        
        if new_lat != '' and new_long != '':
            
            print('de lattitude:', new_lat, 'et de longitude', new_long)
            
            adresse = par_lat_par_long(lat, long)
            adresse = adresse.split()


            lat, long = ville(adresse[-6][:-1])
            print('adresse trouvée :', adresse[-6][:-1], '\n')
            vent, degres_vent = le_vent(adresse[-6][:-1])
            
        else:
            lat, long = ville(i)
            print('de lattitude:', lat, 'de longitude', long, '\n')
            vent, degres_vent = le_vent(i)



        
        #print('vent de :', vent, 'de degres :', degres_vent, '\n')
            
        position_vent = calcul_vent(degres_vent)
        #print('donc le vent va vers:', position_vent, '\n')
        if new_lat != '' and new_long != '':
            nouvelle_position = long_lat(new_lat, new_long, vent, position_vent)
            print('la nouvelle position est de :', nouvelle_position)    
        else:
            nouvelle_position = long_lat(lat, long, vent, position_vent)
            print('la nouvelle position est de :', nouvelle_position)    
        
        new_lat = nouvelle_position[0]
        new_long = nouvelle_position[1]

        
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        

















