from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .carte.direction.vent import *

from .views_function import function_map
from .views_function import function_map2
from .views_function import function_map3



def navebarre_vent(request):
    return render(request, "navebarre_vent.html")

@csrf_exempt
def map(request):

    if request.method == "POST":
        
 
        data = request.POST.get('data')
        data2 = request.POST.get('a')

        if data:
            nouvelle_position, lat, long = function_map(data)
   
            return HttpResponse((lat,' ', long, ' ', nouvelle_position))

        if data2:

            lat, long, listee, index = function_map2(data2)     
            nouvelle_position, lat, long = function_map3(lat, long, listee, index, data)
                    
            return HttpResponse((lat,' ', long, ' ', nouvelle_position))










    return render(request, "map.html")



def essais(request):
    return render(request, "essais.html")


if __name__=="__main__":
    map(request)
    essais(request)

    
