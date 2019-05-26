from geopy.geocoders import Nominatim
import requests
from bs4 import *

def ville(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""

    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()
    
    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var

    b = location.latitude
    c = location.longitude

    
    print(b, c)
    return b, c



def recherche(lieu):
    
    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()


    vent = data['wind']['speed']
    deg = data['wind']['deg']

    print(vent, deg)



    

def par_lat_par_long(lat, long):

    path = 'https://nominatim.openstreetmap.org/reverse?format=xml&lat={}&lon={}&zoom=18&addressdetails=1'
    path = path.format(lat, long)
    
    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    liste = []
    liste.append(soup.text)
    
    liste = liste[0][4:]
    
    liste1 = []
    mot = ''

    c = 0
    for i in liste:
    
        if i == ' ':
            liste1.append(mot)
            mot = ''
        else:
            mot += i
            
        c+=1



    liste2 = []
    code = ''
    for i in liste1:
       
        try:
            i = int(i[:-1])
            if i == int(i):
                break

        except:
            pass

        
        liste2.append(i)



        
    print(liste2[-6][:-1])
            


#while calcul vent possible

    
pos = ville('crest')#site pollué
recherche('crest') #vent
#calcul vent
par_lat_par_long(pos[0], pos[1])#calcul via degres et m/s



















