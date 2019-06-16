import requests
from bs4 import *
import datetime


LISTE1 = ['coiffure', 'COIFFURE', 'salon', 'salon de coiffure',
         'Franck Provost', 'coiffeur', 'hairdresser', 'prestige', 'Prestige',
          'hair', 'bambo', 'haircut', 'Hair', 'Hairdresser', 'Coiffure',
          'Coiffeur', 'Hairdressers', 'coiffeuse']


def cities(city):
    path = 'https://www.google.com/search?q={}+coiffeur&oq={}+coiffeur'
    path = path.format(city, city)

    r = requests.get(path)
    page = r.content
    
    soup = BeautifulSoup(page, "html.parser")
    
    Property = soup.find_all("span")

    liste = []

    for i in Property:
        print(i.string)
        for j in LISTE1:
            a = str(i.string).find(str(j))
            if a >= 0:
                liste.append(i.string)
    print(liste)
    return liste #coiffeur dans ces villes

def schedule_hair(name, city):

    path = 'https://www.google.com/search?ei=Gnn5XJP5KIu5gweW1qaQBQ&q={0}+{1}+horraires&oq={0}+{1}+horraires'

    path = path.format(name, city)

    #print(path)

    r = requests.get(path, headers={
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
     })
    page = r.content

    soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")

    Property = soup.find_all("td")

    liste = []
    for i in Property:
        print(i.string)
        liste.append(i.string)


##    week = ['lundi',
##              'mardi',
##              'mercredi',
##              'jeudi',
##              'vendredi',
##              'samedi',
##              'dimanche',
##             ]



    week = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
             ]

    day = ''
    p = ''
    liste1 = []
    c = 0
    for i in liste:
        hour = ''
        #print(i)
        #print('\n')
        for j in week:
            a = str(i).find(str(j))
            if a >= 0:
                if i == 'Monday':
                    p = 'lundi'
                elif i == 'Tuesday':
                    p = 'mardi'
                elif i == 'Wednesday':
                    p = 'mercredi'
                elif i == 'Thursday':
                    p = 'jeudi'
                elif i == 'Friday':
                    p = 'vendredi'
                elif i == 'Saturday':
                    p = 'samedi'
                elif i == 'Sunday':
                    p = 'dimanche'
                
                liste1.append([p, liste[c+1]])
                #liste1.append([i, liste[c+1]])
            
        c+=1
      
       
    print(liste1)
    return liste1



#HERE THERE ARE OPTIONAL function we dont call it
def numero(nom, ville):
    
    path = "https://annuaire.118712.fr/?s={}+{}"
    path = path.format(nom, ville)

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




def rayon(ville):
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









#la_ville = 'eurre'


#alentour = rayon(la_ville)
#print(alentour)
##

#les_coiffeurs = ville('crest')
    
    


#print(les_coiffeurs)
##les_coiffeurs = ville('valence')
##print(les_coiffeurs)
##    
##for i in les_coiffeurs:
##    a = horraire(i, 'valence')
##    print(a)
#print(numero('Coiffure Marilyne', 'crest'))








