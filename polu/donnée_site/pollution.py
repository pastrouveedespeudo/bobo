import requests
import urllib.request
from bs4 import *
import datetime


CLE = '5a72ceae1feda40543d5844b2e04a205'


def taux_particule(lieu):
    
    liste = []
    nb = []
    
    path = "https://air.plumelabs.com/fr/live/{}".format(lieu)
    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'report__pi-number'})
    for i in propriete:
        liste.append(i.get_text())
    for i in liste:
        for j in i:
            try:
                j = int(j)
                if j == int(j):
                    nb.append(str(j))
            except:
                pass
            
    nb = ''.join(nb)
    nb = int(nb)
    polution = nb

 
    return polution

def pression_ville(lieu):
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,CLE)
    r = requests.get(localisation)
    data=r.json()
    
    pression = data['main']['pressure']
    return pression

def temps_ville(lieu, donnée):
    
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,CLE)
    r = requests.get(localisation)
    data=r.json()

    if donnée == 'vent':
        vent = data['wind']['speed']
        return vent
    
    elif donnée == 'météo':
        méteo = data['weather'][0]['main']

        data = ''
        
        if méteo == 'Clouds' or méteo == 'Mist':
            data = 'Nuageux'
        elif méteo == 'Rain' or méteo == 'Thunderstorm'\
             or méteo == 'Haze':
            data = 'Pluie'
        elif méteo == 'Clear':
            data = 'Beau temps'

        
        return  data

def climat_ville(lieu):
    
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(lieu,CLE)
    r = requests.get(localisation)
    data=r.json()

    température = data['main']['temp']
    température = température - 273.15

    return température

        
def saison():

    date = datetime.datetime.now()
    mois = date.month
    jour = date.day

   
    
    if mois == 12 or mois == 1\
       or mois == 2:
        return 'hiver'

    elif mois == 3 or mois == 4\
         or mois == 5:
        return 'primtemps'

    elif mois == 6 or mois == 7\
         or mois == 8\
         or mois == 9:
        return 'été'

    elif mois == 10 or mois == 11\
         or mois == 12:
        return 'automne'

def traffique(lieu):
    
    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute



    heure = heure + 2
    heure_pointe_semaine = [7,8,9,16,17,18,19]

    départ_routier = [(2,1), (5,1), (9,2), (16,2), (22,2),(23,2),
                      (1,3),(2,3),(8,3),(9,3),
                      (19,4),(22,4),(26,4),(27,4),(28,4),
                      (4,5),(5,5),(29,5),(30,5),
                      (5,6),(6,6),(7,6),(10,6),(28,6),
                      (5,7),(6,7),(7,7),(12,7),(13,7),(14,7),(19,7),(20,7),(21,7),(26,7),(27,7),(28,7),
                      (2,8),(3,8),(4,8),(9,8),(10,8),(11,8),(16,8),(17,8),(18,8),(19,8),(23,8),(24,8),(25,8),(30,8),(31,8),
                      (1,9),
                      (18,10),(25,10),(26,10),(31,10),
                      (3,11),(8,11),(11,11),
                      (20,12),(21,12),(22,12),(24,12),(27,12),(28,12)
        ]


    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""

    
    for i in départ_routier:
        if (jour, mois) == i :
            dep = 'Oui'

        elif (jour, mois) != i :
            normale = 'Oui'
            dep = 'Non'
            

    for i in heure_pointe_semaine:

        if i == heure:
            pointe = 'Oui'
            non_pointe = 'Non'
            break
        

    if pointe == '':
        pointe = 'Non'
        non_pointe = 'Oui'





    return dep, pointe, normale, non_pointe



def habitude():

    weekend = ''
    jour_de_semaine = ''
    
    pointe = [8,9,16,17,18,19]#reverifie les pointes
    jour = ['samedi', 'dimanche']

    
    date = datetime.datetime.now()

    heure = date.hour
    jour = date.weekday()
   
    #print(heure, jour)

    if jour == 5 or jour == 6:
        weekend = 'Weekend'
        jour_de_semaine = 'Non'
        
    else:
        weekend = 'Non'
        jour_de_semaine = 'Oui'


    return weekend, jour_de_semaine


def ville_pollué_classement(lieu):

    liste = ["paris", "marseille", "grenoble", "mulhouse",
             "marignane","strasbourg","lyon"]

    for i in liste:
        if lieu == i:
            indexe = liste.index(i)
    
    
    return indexe + 1



def region_industrielle(lieu):


    site = ''
    
    pole_poluant = ['Nord',
                    'Bouches-du-Rhône',
                    'Moselle',
                    'Seine-Maritime',
                    'Loire-Atlantique',
                    'Haute-Normandie',
                    'Meurthe-et-Moselle',
                    'Seine-Maritime',
                    'Rhône'
                    ]




    path = "https://fr.wikipedia.org/wiki/{}".format(lieu) 

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find('table',attrs={"class":u"infobox_v2"})
    propriete = str(propriete)
   
  
    for i in pole_poluant:
        a = str(propriete).find(str(i))
        if a > 0:
            site = 'oui'
            return site

    site = 'non'
    return site


def requete_lyon_traffique(path):

    liste = []
    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find('div',attrs={"class":u"news"})
    
    
    #agissement = str(propriete).find(str("pollution"))
    #agissement2 = str(propriete).find(str("circulation différenciée"))

    #if agissement >= 0 and agissement2 >= 0:
    #    ACTIVITE_EXEPTIONNELLE['aggissement'] += 1



    trafic = str(propriete).find(str("circulation"))
    trafic1 = str(propriete).find(str("dense"))
    trafic2 = str(propriete).find(str("très dense"))

    #if trafic >= 0 and trafic1 >= 0 or trafic2 >= 0:
    #    ACTIVITE_EXEPTIONNELLE['circulation dense'] += 1

    manif = str(propriete).find(str("Manifestation"))
    manif1 = str(propriete).find(str("manifestation"))


    if manif >= 0 or manif1 >=0 :
        return 'il y a une manifestation'
    else:
        return 'non pas manifestation'

    news = [str(propriete)]
    nombre = news[0][160:165]
    nombre2 = []
    for i in nombre:
        
        try:
            i = int(i)
            nombre2.append(i)

        except:
            pass

    
    #if nombre2[0] > 0:
    #    ACTIVITE_EXEPTIONNELLE['condition a polution'] += 1




    
def requete_paris_traffique(path):

    semaine = {'lundi':0, 'mardi':1, 'mercredi':2, 'jeudi':3, 'vendredi':4, 'samedi':5,
               'dimanche':6}

    liste = [[],[]]
    
    date = datetime.datetime.now()
    jour = date.day
    jour_semaine = date.weekday()


    liste = []
    r = requests.get(path)
    

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("table")
   

    for i in propriete:
        date = soup.find('span',attrs={"class":u"wday"})
    


    date = str(date)


    lundi = str(date).find("lundi")
    mardi = str(date).find("mardi")
    mercredi = str(date).find("mercredi")
    jeudi = str(date).find("jeudi")
    vendredi = str(date).find("vendredi")
    samedi = str(date).find("samedi")
    dimanche = str(date).find("dimanche")
    
    if lundi > 0 :
        a = 0
    if mardi > 0 :
        a = 1
    if mercredi > 0 :
        a = 2
    if jeudi > 0 :
        a = 3
    if vendredi > 0 :
        a = 4
    if samedi > 0 :
        a = 5
    if dimanche > 0 :
        a = 6

    numero_mois = [date]
    
    numero_mois = numero_mois[0][23:42]


    num = []
   
    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)
            
        except:
            pass

    #print(type(num[0]))
    #print(num)
    #print(a)


    if a == jour_semaine and num[0] == jour:
        return 'il y a une manifestation'
    else:
        return 'non pas manifestation'
       
    #a dans 9 jours hihi faut faire pour le 10 par ex


def requete_marseille_traffique(path):
    r = requests.get(path)

    date = datetime.datetime.now()
    jour = date.day
    jour_semaine = date.weekday()
    
    
    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    date = soup.find('div',attrs={"class":u"ml-agenda-date-page"})
   
    date = str(date)
    
    a = 0
    lundi = str(date).find("lundi")
    mardi = str(date).find("mardi")
    mercredi = str(date).find("mercredi")
    jeudi = str(date).find("jeudi")
    vendredi = str(date).find("vendredi")
    samedi = str(date).find("samedi")
    dimanche = str(date).find("dimanche")
    
    if lundi > 0 :
        a = 0
    if mardi > 0 :
        a = 1
    if mercredi > 0 :
        a = 2
    if jeudi > 0 :
        a = 3
    if vendredi > 0 :
        a = 4
    if samedi > 0 :
        a = 5
    if dimanche > 0 :
        a = 6


    numero = soup.find('div',attrs={"class":u"ml-agenda-date-page"})
    #print(numero)
    numero = str(numero)
    numero = numero[20:]
    
    try:
        numero = int(numero)
    except:
        liste = []
        numero = str(numero)

        for i in numero:
            try:
                i = int(i)
                liste.append(i)
            except:
                pass
    #print(a)
    if a == jour_semaine and liste[0] == jour:
        return 'il y a une manifestation'
    else:
        return 'non pas manifestation'

def activité_execptionnelle(lieu):
    
    if lieu == "lyon":
        path = "https://www.onlymoov.com/trafic/"
        a = requete_lyon_traffique(path)

        return a

        

    elif lieu == "paris":
        path = "https://paris.demosphere.net/manifestations-paris"
        a = requete_paris_traffique(path)

        return a

    
    elif lieu == "marseille":
        path = "https://mars-infos.org/spip.php?page=agenda"
        a = requete_marseille_traffique(path)

        return a



def socio(lieu):

    lyon = 328469
    paris = 1350800 
    marseille = 762480 

    if lieu == 'lyon':
        return lyon

    if lieu == 'paris':
        return paris

    if lieu == 'marseille':
        return marseille
    #population active de 15 a 59 ans









def bouchons(lieu):

    if lieu == "lyon":
        path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(lieu)
      
        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        propriete = soup.find("span", {'class':'font38 green'})
        liste = []
        print(propriete)
        try:
            for i in propriete:
                for j in i:
                    if j == ',':
                        liste.append(str('.'))
                    try:
                        j = int(j)
                        if j == int(j):
                            liste.append(str(j))
                    except:
                        pass
            liste = "".join(liste)
            print(liste,'000000000000000')
            try:
                b = float(liste)
                print(b)
            except:
                b = int(liste)
                print(b)

        except:
            b = 0
        
        return b




    elif lieu == "paris":
    
        path = "http://www.sytadin.fr/sys/barometre_courbe_cumul.jsp.html#"

        r = requests.get(path)

        liste = []

        page = r.content
        soup = BeautifulSoup(page, "html.parser")

        liste.append(str(soup))
        bouchon = liste[0][1870:1890]
        bouchon = str(bouchon)

        kmbouchon = []
        liste = []
        for i in bouchon:
            try:
                i = int(i)
                kmbouchon.append(str(i))
            except:
                pass

        kmbouchon = "".join(kmbouchon)
        
        try:
            kmbouchon = int(kmbouchon)
        except:
            pass
        b = kmbouchon
           
        return b












































































