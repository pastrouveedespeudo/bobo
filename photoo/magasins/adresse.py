import requests
from bs4 import *
from geopy.geocoders import Nominatim

def addresse_geo(nom, ville):
    path = "https://www.google.com/search?q=adresse+{}+{}+&oq=adresse+{}+{}"
    path = path.format(nom, ville, nom, ville)
    print(path)
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("span")

    mot = 'Address'
    motfr = 'Adresse'
    addresse = ''
    c = 0
    for i in propriete:
        print(i.string)
        if c == 2:
            addresse += i.string
            break
        a = str(i.string).find(str(mot))
        b = str(i.string).find(str(motfr))
        if a >= 0 or b >= 0:
            c += 1

    print(addresse)
    return addresse


def ville_geo(parametre):
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

    
    print(b,c)
    return b, c





#addresse('lof coiffure', 'crest')
#ville('Avenue Félix Rozier, 26400 Crest')





