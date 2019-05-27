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
    print(liste)
    try:
        print(liste2[-6][:-1])
    except:
        pass
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
    
    kilometre = km / 1000 * 0.009
    print('metre, kilometre: ',km, kilometre)

    
    if sens == 'nord':
        lat1 = km
        nouvel_lat = lat + lat1
        print('newlat, long', nouvel_lat, long)


    elif sens == 'nordnordest':
        lat = lat + km
        long = long + km * cos(radians(67.7))
        print('newlat, long', lat, long)
    
    elif sens == 'nordest':
        lat = lat + km
        long = long + km * cos(radians(45))
        print('newlat, long', lat, long)
        
    elif sens == 'estnordest':
        lat = lat + km
        long = long + km * cos(radians(22.5))
        print('newlat, long', lat, long)
    
    elif sens == 'est':
        long = long + km
        print('lat, newlong', lat, long)
        
    elif sens == 'estsudest':
        lat = lat + km * cos(radians(157.5))
        long = long + km
        print('newlat, long', lat, long)
        
    elif sens == 'sudest':
        lat = lat + km * cos(radians(135))
        long = long + km
        print('newlat, long', lat, long)
        
    elif sens == 'sudsudest':
        lat = lat + km * cos(radians(112.5))
        long = long + km
        print('newlat, long', lat, long)
    
    elif sens == 'sud':
        lat1 = km
        nouvel_lat = lat - lat1
 
        print('newlat, long', nouvel_lat, long)




    elif sens == 'sudsudouest':
        lat = lat + km * cos(radians(247.5))
        long = long + km
        print('newlat, long', lat, long)

        
    elif sens == 'sudouest':
        lat = lat + km * cos(radians(225))
        long = long + km
        print('newlat, long', lat, long)
        
    elif sens == 'ouestsudouest':
        lat = lat + km * cos(radians(202.5))
        long = long + km
        print('newlat, long', lat, long)


    
    elif sens == 'ouest':
        kilo = km
        long1 = long - kilo
        print('lat, newlong', lat, long1)

        
    elif sens == 'ouestnordouest':
        lat = lat + km
        long = long + km * cos(radians(337))
        print('newlat, long', lat, long)
        
    elif sens == 'nordouest':
        lat = lat + km
        long = long + km * cos(radians(315))
        print('newlat, long', lat, long)
        
    elif sens == 'nordnordouest':
        lat = lat + km
        long = long + km * cos(radians(292.5))
        print('newlat, long', lat, long)





    
#while calcul vent possible

    
lat, long = ville('Université Catholique de Lyon, 69002 Lyon')#site pollué
##vitesse_vent, degres = recherche('crest') #vent
##degres = calcul_vent(degres)
##par_lat_par_long(lat, long)#calcul via degres et m/s
##long_lat(lat, long, vitesse_vent, degres)

#par_lat_par_long('44.7282675', '5.0236641')
par_lat_par_long('45.74697512807942', '4.824759000000001')





























