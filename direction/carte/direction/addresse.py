from geopy.geocoders import Nominatim
import requests
from bs4 import *
from math import *


def par_lat_par_long(lat, long):

    path = 'https://nominatim.openstreetmap.org/reverse?format=xml&lat={}&lon={}&zoom=18&addressdetails=1'
    path = path.format(lat, long)
    
    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    liste = []
    liste.append(soup.text)
    
    liste = liste[0][2:]
    
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


  

    return ' '.join(liste2)
