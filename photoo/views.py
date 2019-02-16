from django.shortcuts import render
from .photo import *

def photo(request):
    if request.method == "POST":

        recherche = request.POST.get('im')
        print("OUIIIIIIIIIIIIII", recherche)

        capture()
    return render(request, 'photo.html')


def essais(request):
    return render(request, 'essais.html')
