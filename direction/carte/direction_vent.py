from geopy.geocoders import Nominatim
import requests
from bs4 import *
from math import *


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

    
    print('origine', b,c)
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
    
    liste = liste[0]
    
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
    return liste2[-6][:-1]       

def calcul_vent(direction):


    if direction == 0 or direction == 360:
      
        return 'nord'


    elif direction > 0 and direction <= 22.5:
      
        return 'nordnordest'
    
    elif direction > 22.5 and direction <= 45:
      
        return 'nordnordest'
    
    elif direction == 45:
     
        return 'nordest'

    
    elif direction > 45 and direction <= 67.5:
     
        return 'estnordest'
    
    elif direction > 67.5 and direction <= 90:
  
        return 'estnordest'
    
    elif direction > 90 and direction <= 112.5:
        
        return 'est'
    
    elif direction > 112.5 and direction <= 135:
     
        return 'estsudest'
    
    elif direction == 135:
        
        return 'sudest'

    
    elif direction > 135 and direction <= 157.5:
       
        return 'sudsudest'

    
    elif direction > 157.5 and direction <= 180:
      
        return 'sudsudest'

    
    elif direction == 180:
      
         return 'sud'
         
    elif direction > 180 and direction <= 202.5:
    
        return 'sudsudouest'

    
    elif direction > 202.5 and direction <= 225:
     
        return 'sudsudouest'
    
    elif direction == 225:
        
        return 'sudouest'

    elif direction > 225 and direction <= 247.5:
       
        return 'sudouest'
    
    elif direction > 247.5 and direction <= 270:
     
        return 'ouestsudouest'
    
    elif direction > 270:
      
        return 'ouest'
    
    elif direction > 270 and direction <= 292.5:
      
        return 'ouestnordouest'
    
    elif direction > 292.5 and direction <= 315:
  
        return 'nordouest'
    
    elif direction == 315:

        return 'nordouest'
    
    elif direction > 315 and direction <= 337.5:
        return 'nordnordouest'
    
    #print('degres : ',degres)




   

def long_lat(lat, long, km, sens):


    print(sens)
    
    kilometre = km / 1000
    print('metre, kilometre: ',km, kilometre)

    
    if sens == 'nord':
        lat1 = km*0.009
        nouvel_lat = lat + lat1
        long1 = 111.11 * cos(radians(nouvel_lat))
        print('newlat, long', nouvel_lat, long)


    elif sens == 'nordnordest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(22.5)) + kilo
        print('newlat, long', lat, long1 )
    
    elif sens == 'nordest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(45)) + kilo
        print('newlat, long', lat, long1 )
        
    elif sens == 'estnordest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(67.5)) + kilo
        print('newlat, long', lat, long1 )
    
    elif sens == 'est':
        long1 = 111.11 * cos(radians(lat) + km*0.009)
        print('lat, newlong', lat, long)
        
    elif sens == 'estsudest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(112.5)) + kilo
        print('newlat, long', lat, long1 )
        
    elif sens == 'sudest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(157.5)) + kilo
        print('newlat, long', long1 )
        
    elif sens == 'sudsudest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(202.5)) + kilo
        print('newlat, long', lat, long1 )
    
    elif sens == 'sud':
        lat1 = km*0.009
        nouvel_lat = lat - lat1
        long1 = 111.11 * cos(radians(nouvel_lat))
        print('newlat, long', nouvel_lat, long)

        
    elif sens == 'sudsudouest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(202.5)) + kilo
        print('newlat, long', lat, long1 )

        
    elif sens == 'sudouest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(225)) + kilo
        print('newlat, long', lat, long1 )
        
    elif sens == 'ouestsudouest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(247.5)) + kilo
        print('newlat, long', lat, long1 )
    
    elif sens == 'ouest':
        long1 = 111.11 * cos(radians(lat) - km*0.009)
        print('lat, newlong', lat, long)

        
    elif sens == 'ouestnordouest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(292.5)) + kilo
        print('newlat, long', lat, long1 )
        
    elif sens == 'nordouest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(315)) + kilo
        print('newlat, long', lat, long1 )
        
    elif sens == 'nordnordouest':
        kilo = km*0.009
        long1 = 111.11 * cos(radians(337)) + kilo
        print('newlat, long', lat, long1 )





    
#while calcul vent possible

    
lat, long = ville('crest')#site pollué
vitesse_vent, degres = recherche('crest') #vent
degres = calcul_vent(degres)
par_lat_par_long(lat, long)#calcul via degres et m/s
long_lat(lat, long, vitesse_vent, degres)































