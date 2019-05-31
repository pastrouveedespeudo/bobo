from geopy.geocoders import Nominatim
import requests
from bs4 import *
from math import *


def le_vent(lieu):
    print(lieu)
    clé = '5a72ceae1feda40543d5844b2e04a205'
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,clé)
    r = requests.get(localisation)
    data=r.json()


    vent = data['wind']['speed']
    deg = data['wind']['deg']

    #print(vent, deg)
    return vent, deg









def code_postal(lieu):
    path = 'http://code.postal.fr/code-postal-{}'
    path = path.format(lieu)
    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("h2")


    liste = []
    liste.append(propriete)

    code = ''
    liste_code = []
    for i in liste[0]:
        for j in i:
            for k in j:
                try:
                    k = int(k)
                    if k == int(k):
                        code += str(k)
                        
                except:
                    if code != '':
                        liste_code.append(code)
                        code = ''
                    else:
                        pass
 

    return liste_code[0]


    
def vent_deux(lieu):
    path = 'https://www.lameteoagricole.net/meteo-heure-par-heure/{}-{}.html'

    
    code = code_postal(lieu)

    path.format(lieu, code)

    
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("div", {"class":"fond2"})


    liste = []
    liste.append(propriete)

    liste1 = []
    mot = ''
    c = 0
    for i in liste[0]:
        for j in i:
            a = str(j).find('Vent :')
            if a >= 0:
                for k in j:
                    if k == " ":
                        if mot == 'N':
                            return '' 'nord'
                        elif mot == 'NNE':
                            return 'nordnordest' 
                        elif mot == 'NE':
                            return 'nordest'
                        elif mot == 'ENE':
                            return 'estnordest'
                        elif mot == 'E':
                            return 'est'
                        elif mot == 'ESE':
                            return 'estsudest'
                        elif mot == 'SE':
                            return 'sudest'
                        elif mot == 'SSE':
                            return 'sudsudest'
                        elif mot == 'S':
                            return 'sud'
                        elif mot == 'SSO':
                            return 'sudsudouest'
                        elif mot == 'SO':
                            return 'sudouest'
                        elif mot == 'OSO':
                            return 'ouestsudouest'
                        elif mot == 'O':
                            return 'ouest'
                        elif mot == 'ONO':
                            return 'ouestnordouest'
                        elif mot == 'NO':
                            return 'nordouest'
                        elif mot == 'NNO':
                            return 'nordnordouest'
   





                        
                        mot = ''
                    else:
                        mot += k

   
                break
            
























#le_vent('crest')
#a = vent_deux('valence')
#print(a)
#code_postal('aouste sur sye')










