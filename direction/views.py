from django.shortcuts import render
from django.http import HttpResponse


from .carte.direction.ville import ville
from .carte.direction.nouvel_pos import long_lat
from .carte.direction.boussole import calcul_vent
from .carte.direction.vent import *

from .carte.direction.superficie import *
from .carte.direction.addresse import *



def map(request):

    if request.method == "POST":
        print('yooooooooooooooooooo')
        data = request.POST.get('data')
        print(data)

        lat, long = ville(data)
        print(lat, long)
        adresse = dress_to_ville(lat, long)
        print(adresse)
        position_vent = vent_deux(data)
        print(position_vent)
        vent = superficie_ville(adresse[1])
        print(vent)
        nouvelle_position = long_lat(lat, long, vent, position_vent)




        return HttpResponse((lat,' ',
                             long, ' ',
                             adresse, ' ',
                             position_vent, ' ',
                             vent, ' ',
                             nouvelle_position))















    return render(request, "map.html")






if __name__=="__main__":
    map(request)
