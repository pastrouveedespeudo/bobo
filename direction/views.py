from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .carte.direction.ville import ville
from .carte.direction.nouvel_pos import long_lat


from .carte.direction.boussole import calcul_vent
from .carte.direction.vent import *

from .carte.direction.superficie import *
from .carte.direction.addresse import *
 

@csrf_exempt
def map(request):

    if request.method == "POST":
        
        print('yooooooooooooooooooo')
        data = request.POST.get('data')
        data2 = request.POST.get('a')
        print(data2, '00000000000000000000000000000000000000000000000')
        print(data)

        if data:
            lat, long = ville(data)
            print(lat, long)
            adresse = dress_to_ville(lat, long)
            print(adresse)
            position_vent = vent_deux(data)
            print(position_vent)
            vent = superficie_ville(adresse[1])
            print(vent)
            nouvelle_position = long_lat(lat, long, vent, position_vent)
            print(nouvelle_position)



            return HttpResponse((lat,' ',
                                 long, ' ',
                                 nouvelle_position))

        if data2:
            print('OUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
            print(data2)


            lat = ''
            long = ''
            for i in data2:
                if i == ',':
                    break
                elif i == '.':
                    lat += i
                else:
                    lat += i
                    
            listee = []
            c = 0
            for i in data2:
                
                if i == ',':
                    index = c
                else:
                    listee.append(i)
                c+=1
                

                    

            lat = float(lat)
            
            long = listee[index:-1]
            
            long = "".join(long)
            long = float(long)

            print(lat, long,'0001325123132132132123132132')

            adresse = dress_to_ville(lat, long)
            print(adresse)
            
            position_vent = vent_deux(data)
            print(position_vent)
            vent = superficie_ville(adresse[1])
            print(vent)
            nouvelle_position = long_lat(lat, long, vent, position_vent)
            print(nouvelle_position)


            return HttpResponse((lat,' ',
                                 long, ' ',
                                 nouvelle_position))










    return render(request, "map.html")



def essais(request):
    return render(request, "essais.html")


if __name__=="__main__":
    map(request)
    essais(request)

    
