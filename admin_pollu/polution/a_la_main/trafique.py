import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops



def trafique_circulation():

    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute




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


    #print(jour, mois, année)
    #print(str(heure) + ":" + str(minute))



    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""

    
    for i in départ_routier:
        if (jour, mois) == i :
            dep = True

    if dep == '':
        normale = True


    if dep == True:
        return 'depart_routier'
 
    elif normale == True: 
        return 'regulier jour'





def heure_de_pointe():

    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""


    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute


    heure_pointe_semaine = [7,8,9,16,17,18,19]


       
    for i in heure_pointe_semaine:
        if i == heure:
            pointe = True

    if pointe != True:
        non_pointe = True

          
    if pointe == True:
        return 'heure_pointe'
        
        
    elif non_pointe == True:
        return 'non_heure_pointe'
   


def habitude():


    jour = ['samedi', 'dimanche']

    
    date = datetime.datetime.now()

    heure = date.hour
    jour = date.weekday()
   
    if jour == 5 or jour == 6:
        return 'weekend'
    else:
        return 'jour_semaine'
        #si ca continue c ici


def bouchons(lieu):


  
    if lieu == "lyon":
        path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(lieu)
      
        r = requests.get(path)



        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        propriete = soup.find("span", {'class':'font38 green'})
        liste = []
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
            #print(liste,'00000000000000000000000000000000000000000000')
            try:
                b = float(liste)
                #print(b)
            except:
                b = int(liste)
                #print(b)

        except:
            b = 0
        
        if b == 0 or b == 0.0:
            return 'non'

    
        elif b > 0  and b <= 5.0:
            return 'petit'


        elif b > 5 and b <= 9.0:
            return 'moyen'

        elif b > 9 and b <= 15.0:
            return 'grand'

        elif b > 15 and b <= 20.0:
            return 'assez grand'

        elif b > 20.0:
            return 'tres grand'

    elif lieu == "marseille":
        return 'moyen'


    elif lieu == "paris":
    
        path = "http://www.sytadin.fr/sys/barometre_courbe_cumul.jsp.html#"

        r = requests.get(path)

        liste = []

        page = r.content
        soup = BeautifulSoup(page, "html.parser")

        liste.append(str(soup))
        bouchon = liste[0][1872:1878]
        
        bouchon = str(bouchon)
        print(bouchon)
        kmbouchon = []
        liste = []
        for i in bouchon:
            #print(i)
            try:
                i = int(i)
                kmbouchon.append(str(i))
            except:
                pass

        kmbouchon = "".join(kmbouchon)
        #print(kmbouchon,'000000000000000000000000000000000000000000000')
        kmbouchon = int(kmbouchon)

        b = kmbouchon
       
        if b == 0 or b == 0.0:
            return 'non'

        elif b > 0  and b <= 5:
            return 'petit'

        elif b > 5 and b <= 9:
            return 'moyen'

        elif b > 9 and b <= 15:
            return 'grand'

        elif b > 15 and b <= 20:
            return 'assez grand' 

        elif b > 20:
            return 'tres grand' 
                   



def requete_lyon_traffique(path):


    liste = []
    r = requests.get(path)


    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find('div',attrs={"class":u"news"})
    
    trafic = str(propriete).find(str("circulation"))
    trafic1 = str(propriete).find(str("dense"))
    trafic2 = str(propriete).find(str("très dense"))

    manif = str(propriete).find(str("Manifestation"))
    manif1 = str(propriete).find(str("manifestation"))


    if manif >= 0 or manif1 >=0 :
        return 'manifestation'
    else:
        return 'non_manifestation'

    news = [str(propriete)]
    nombre = news[0][160:165]
    nombre2 = []
    for i in nombre:
        
        try:
            i = int(i)
            nombre2.append(i)

        except:
            pass



    
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
        return 'manifestation'
    else:
        return 'non_manifestation'

    #print(ACTIVITE_EXEPTIONNELLE)
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
        return 'manifestation'
    else:
        return 'non_manifestation'

def activité_execptionnelle(lieu):


    
    if lieu == "lyon":
        path = "https://www.onlymoov.com/trafic/"
        a = requete_lyon_traffique(path)

        

    elif lieu == "paris":
        path = "https://paris.demosphere.net/manifestations-paris"
        a = requete_paris_traffique(path)

    elif lieu == "marseille":
        path = "https://mars-infos.org/spip.php?page=agenda"
        a = requete_marseille_traffique(path)

    return a




bouchons("paris")






