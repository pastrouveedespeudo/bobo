from geopy.geocoders import Nominatim
import requests
from bs4 import *
from math import *

from .CONFIG import CLE
from .CONFIG import PATH_VENT
from .CONFIG import PATH_POSTAL
from .CONFIG import PATH_VENT_DEUX
from .CONFIG import VENT_DEUX_RECHERCHE

def le_vent(lieu):

    
    localisation = PATH_VENT.format(lieu, CLE)
    r = requests.get(localisation)
    data=r.json()


    vent = data['wind']['speed']
    deg = data['wind']['deg']

    return vent, deg



def function_code_postal(lieu):
    
    path = PATH_POSTAL.format(lieu)
    
    request_html = requests.get(path)
    page = request_html.content
    
    soup_html = BeautifulSoup(page, "html.parser")
    
    propriete = soup_html.find_all("h2")

    liste = []
    liste.append(propriete)

    return liste


def code_postal(lieu):

    liste = function_code_postal(lieu)
    
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



def function_vent_deux(mot):
    
    if mot == 'N':
        return 'nord'
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

    
def vent_deux(lieu):

    code = code_postal(lieu)
    path = PATH_VENT_DEUX.format(lieu, code)

    request_html = requests.get(path)
    page = request_html.content
    
    soup_html = BeautifulSoup(page, "html.parser")
    
    propriete = soup_html.find_all("td", {"class":"td_corps_meteo"})

    liste = []
    liste.append(propriete)

      
    liste1 = []
    mot = ''
    c = 0
    for i in liste:
        for j in i:
            a = str(j).find(VENT_DEUX_RECHERCHE)
            if a >= 0:
                for k in j:
                    for l in k:
                        mot += l
                break
            
    situation = function_vent_deux(mot)
    return situation


