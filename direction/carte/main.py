
from direction.ville import ville
from direction.addresse import par_lat_par_long
from direction.nouvel_pos import long_lat
from direction.boussole import calcul_vent
from direction.vent import le_vent


liste = ['crest']

for i in liste:
    print('ville cherchée:', i + '\n')

    lat, long = ville(i)
    print('de lattitude:', lat, 'de longitude', long, '\n')

    adresse = par_lat_par_long(lat, long)
    print('adresse trouvée :', adresse, '\n')

    vent, degres_vent = le_vent(i)

    print('vent de :', vent, 'de degres :', degres_vent, '\n')

    position_vent = calcul_vent(degres_vent)
    print('donc le vent va vers:', position_vent, '\n')

    nouvelle_position = long_lat(lat, long, vent, position_vent)
    print('la nouvelle position est de :', nouvelle_position)    
