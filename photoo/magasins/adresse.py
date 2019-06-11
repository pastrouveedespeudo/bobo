import requests
from bs4 import *
from geopy.geocoders import Nominatim

scrap = ['Rue', 'Avenue', 'Allée', 'allée', 'Impasse', 'Adresse']

def addresse_geo(nom, ville):
    path = "https://www.google.com/search?q=adresse+{}+{}+&oq=adresse+{}+{}"
    path = path.format(nom, ville, nom, ville)

    r = requests.get(path, headers={
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
     })
    page = r
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("span")

    stop = ''
    addresse = []

    for i in propriete:
        if stop == True:
            break
        if i.string == None:
            pass
        else:
            for j in scrap:
                a = str(i.string).find(str(j))
                if a >= 0:
                    addresse.append(i.string)
                    stop = True
                    
    print(addresse)
    return addresse


def ville_geo(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""

    print(parametre)
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





#addresse_geo('Hair salon · Avenue Félix Rozier', 'crest')
#ville_geo('106 Rue Professeur Beauvisage')





