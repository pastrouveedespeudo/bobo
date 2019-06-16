import requests
from bs4 import *


GYM = ['fitness', 'gym', 'body','Body', 'musculation', 'Fitness', 'Club', 'Gym',
       'sport', 'Sport', 'Salle', 'salle', 'Salle de sport', 'salle de sport', 'wellness',
       'Wellness', 'Keep cool', 'KEEP COOL', 'keep cool', ]

def rayon(ville):
    """Here it's an optionnal service for more hairdressers
    but we have timeout 30 sec so we let it but
    it doesen't call"""
    
    path = "https://www.villorama.com/ville/{}/villes-proches.html"
    
    path = path.format(ville)
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("a")

    liste = []

    for i in propriete:
        if i.string == None:
            pass
        elif i.string == 'France' or i.string == 'Distance à vol d\'oiseau'\
             or i.string == 'Communes proches' or i.string == 'Présentation'\
             or i.string == 'En bref' or i.string == 'Sport'\
             or i.string == 'Météo' or i.string == 'Prévisions météo'\
             or i.string == 'Sorties culturelles' or i.string == 'Agenda'\
             or i.string == 'Hôtels' or i.string == 'Midi Moins Une'\
             or i.string == 'mentions légales' or i.string == 'Recrutement'\
             or i.string == 'Midi Moins Une' or i.string == 'Gestion des cookies'\
             or i.string == 'Tourisme' or i.string == 'Office de Tourisme'\
             or i.string == 'Distance routière' or i.string == 'Mairie'\
             or i.string == 'Plan' or i.string == 'Itinéraire' or i.string == 'Annuaire Services'\
             or i.string == 'Résultats d\'élections' or i.string == 'Loisirs' or i.string == 'Spectacles'\
             or i.string == 'Concerts' or i.string == 'Théâtre' or i.string == 'Historique météo'\
             or i.string == 'Rencontres' or i.string == 'Autres informations' or i.string == 'Cinéma'\
             or i.string == 'Sites web' or i.string == 'Identifiez-vous' or i.string == 'Votre espace'\
             or i.string == 'Publicité' or i.string == '' or i.string == 'Conditions d\'Utilisation'\
             or i.string == 'Etablir un lien':
             
             
            pass
             
        else:
            liste.append(i.string)

    liste = liste[3:]
    
    return liste #villes aux alentours


def big_city_gym(city):
    """Here we search gym into the cities"""
    
    path = "https://www.google.com/search?ei=w2n6XJ3hMMeOatXLjOgB&q=sale+de+gym+{0}+france&oq=sale+de+gym+{0}+france"


    #We call BS4
    path = path.format(city)
    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")

    #We search all span
    propriete = soup.find_all("span")
    liste1 = []

    #We searching all elements by GLOBAL list gym
    for i in propriete:
        for j in GYM:
            a = str(i.string).find(str(j))
            if a >= 0:
                liste1.append(i.string)
                
    print(liste1)
    return liste1
    
    

def schedule_gym(name, city):
    """We search all schedule from gym found"""

    #BS4 Stuff
    path = 'https://www.google.com/search?ei=Gnn5XJP5KIu5gweW1qaQBQ&q={0}+{1}+horraires&oq={0}+{1}+horraires'

    path = path.format(name, city)
    r = requests.get(path, headers={
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
     })
    page = r.content
    soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
    
    #propriete = soup.find_all("span")
    propriete = soup.find_all("td")

    liste = []
    for i in propriete:
        liste.append(i.string)

    #This is for local version
##    week = ['lundi',          
##              'mardi',
##              'mercredi',
##              'jeudi',
##              'vendredi',
##              'samedi',
##              'dimanche',
##             ]



    #This is for linux version
    week = ['Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday',
              'Sunday',
             ]


    day = ''

    #We search all tag who comports
    #elements by week list
    liste1 = []
    c = 0
    for i in liste:
        hour = ''

        for j in week:
            a = str(i).find(str(j))
            if a >= 0:
                liste1.append([i, liste[c+1]])
                
        c+=1
      
       
    print(liste1)
    return liste1

    


def number_gym(name, city):
    """Here again it's an optional function
    we dont call it"""
    
    path = "https://annuaire.118712.fr/?s={}+{}"
    path = path.format(name, city)

    r = requests.get(path, headers={
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
     })
    page = r.content
  
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("span")

    liste = []
    for i in propriete:
        if i.string == None:
            pass
        else:
            liste.append(i.string)
            
    tel = ''

    fini = ''
    for i in liste:

        c = 0
        for j in i:
            try:
                
                a = int(i[0])
                b = int(i[1])
                c = int(i[3])
                d = int(i[4])
                e = int(i[6])
                f = int(i[7])
                g = int(i[9])
                h = int(i[10])
                ii = int(i[12])
                j = int(i[13])
                
                if a == int(a) and b == int(b) and\
                    c == int(c) and d == int(d) and\
                    e == int(e) and f == int(f) and\
                    g == int(g) and h == int(h) and\
                    ii == int(ii) and j == int(j):
                    tel += i
                    fini = True
                    break
            except:
                pass
            c += 1
        if fini == True:
            break

    print(tel,'11111111111111111111')
    return tel





















#a = rayon('crest')
#print(a)
#grande_ville_gym('crest')
#horraire_gym("Body's Studio", "crest")
#numero("Body's Studio", "crest")






















