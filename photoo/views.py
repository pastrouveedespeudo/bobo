from django.shortcuts import render
from .photo import *


def mes_images(request):
    return render(request, 'mes_images.html')




def photo(request):
    if request.method == "POST":

        recherche = request.POST.get('im')
        print(recherche,"000000000000000000000000000000000000000000000000000")
        a = capture()
        print(a,)
        return render(request, 'mes_images.html', {'a':a})


    
    return render(request, 'photo.html')


def essais(request):
    return render(request, 'essais.html')
