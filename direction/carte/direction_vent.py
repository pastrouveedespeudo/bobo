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


    return vent, deg


    

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
            

def calcul_vent(vitesse_vent, direction):

    km = vitesse_vent / 1000
    print('kilometre: ', km)

    if direction == 0 or direction == 360:
        print('nord')

    elif direction > 0 or direction > 360:
        print('nordnordest')
        
    elif direction > 0 and direction <= 22.5:
        print('nordnordest')

    elif direction > 22.5 and direction <= 45:
        print('nordnordest')

    elif direction == 45:
        print('nordest')

    elif direction > 45 and direction <= 67.5:
        print('estnordest')

    elif direction > 67.5 and direction <= 90:
        print('estnordest')

    elif direction > 90 and direction <= 112.5:
        print('est')

    elif direction > 112.5 and direction <= 135:
        print('estsudest')

    elif direction == 135:
        print('sudest')

    elif direction > 135 and direction <= 157.5:
        print('sudsudest')

    elif direction > 157.5 and direction <= 180:
        print('sudsudest')

    elif direction == 180:
         print('sud')
         
    elif direction > 180 and direction <= 202.5:
        print('sudsudouest')

    elif direction > 202.5 and direction <= 225:
        print('sudsudouest')
        
    elif direction == 225:
        print('sudouest')


    elif direction > 225 and direction <= 247.5:
        print('sudouest')

    elif direction > 247.5 and direction <= 270:
        print('ouestsudouest')
        
    elif direction > 270:
        print('ouest')
    
    elif direction > 270 and direction <= 292.5:
        print('ouestnordouest')
        
    elif direction > 292.5 and direction <= 315:
        print('norouest')
        
    elif direction == 315:
        print('nordouest')

    elif direction > 315 and direction <= 337.5:
        print('nordnordouest')
    
    print('degres : ',degres)




#while calcul vent possible

    
lat, long = ville('crest')#site pollué
vitesse_vent, degres = recherche('crest') #vent
calcul_vent(vitesse_vent, degres)
par_lat_par_long(lat, long)#calcul via degres et m/s



















