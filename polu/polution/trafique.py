import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops






def trafique_circulation(TRAFIQUE, HEURE):

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


    #print(jour, mois, année)
    #print(str(heure) + ":" + str(minute))



    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""

    
    for i in départ_routier:
        if (jour, mois) == i :
            dep = True

        elif (jour, mois) != i :
            normale = True

    for i in heure_pointe_semaine:
        if i == heure:
            pointe = True
        else:
            non_pointe == True
        

    if dep == True:
        TRAFIQUE['depart_routier'] += 1
 
    elif dep != True and normale == True: 
        TRAFIQUE['regulier jour'] += 1

       

    if pointe == True:
        HEURE['heure_pointe'] += 1
        
        
    elif non_pointe == '' or non_pointe == True:
        HEURE['non_heure_pointe'] += 1
   


def habitude(POINTE, WEEKEND):

    pointe = [8,9,16,17,18,19]#reverifie les pointes
    jour = ['samedi', 'dimanche']

    
    date = datetime.datetime.now()

    heure = date.hour
    jour = date.weekday()
   
    #print(heure, jour)
    pointeTrue = ""
    for i in pointe:
        if heure == i:
            POINTE['pointe'] += 1
            pointeTrue = True
            break

    if pointeTrue != True:
        POINTE['non_pointe'] += 1


    if jour == 5 or jour == 6:
        WEEKEND['weekend'] += 1
    else:
        WEEKEND['non_weekend'] += 1


def bouchons(lieu, BOUCHON):


  
    if lieu == "lyon":
        path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(lieu)
      
        r = requests.get(path)

        km = ''

        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        propriete = soup.find("span", {'class':'font38 green'})
        liste = []
        
        for i in propriete:
            for j in i:
                if j == 'K' or j == 'k':
                    km = True
        
        
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
            try:
                b = float(liste)
                print(b)
            except:
                b = int(liste)
                print(b)

        except:
            b = 0
        
        if km != True:
            b = 0
        
        
        if b == 0 or b == 0.0:
            BOUCHON['non'] += 1 

    
        elif b > 0  and b <= 5:
            BOUCHON['petit'] += 1 


        elif b > 5 and b <= 9:
            BOUCHON['moyen'] += 1 

        elif b > 9 and b <= 15:
            BOUCHON['grand'] += 1 

        elif b > 15 and b <= 20:
            BOUCHON['assez grand'] += 1 

        elif b > 20:
            BOUCHON['tres grand'] += 1

    elif lieu == "marseille":
        BOUCHON['moyen'] += 1 


    elif lieu == "paris":
    
        path = "http://www.sytadin.fr/sys/barometre_courbe_cumul.jsp.html#"

        r = requests.get(path)

        liste = []

        page = r.content
        soup = BeautifulSoup(page, "html.parser")

        liste.append(str(soup))
        bouchon = liste[0][1874:1877]
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
        kmbouchon = int(kmbouchon)

        b = kmbouchon
       
        if b == 0 or b == 0.0:
            BOUCHON['non'] += 1 

        elif b > 0  and b <= 5:
            BOUCHON['petit'] += 1 

        elif b > 5 and b <= 9:
            BOUCHON['moyen'] += 1 

        elif b > 9 and b <= 15:
            BOUCHON['grand'] += 1 

        elif b > 15 and b <= 20:
            BOUCHON['assez grand'] += 1 

        elif b > 20:
            BOUCHON['tres grand'] += 1
                   



def requete_lyon_traffique(path, ACTIVITE_EXEPTIONNELLE):


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
        ACTIVITE_EXEPTIONNELLE['manifestation'] += 1
    else:
        ACTIVITE_EXEPTIONNELLE['non_manifestation'] += 1

    news = [str(propriete)]
    nombre = news[0][160:165]
    nombre2 = []
    for i in nombre:
        
        try:
            i = int(i)
            nombre2.append(i)

        except:
            pass



    
def requete_paris_traffique(path, ACTIVITE_EXEPTIONNELLE):


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
        ACTIVITE_EXEPTIONNELLE['manifestation'] += 1
    else:
        ACTIVITE_EXEPTIONNELLE['non_manifestation'] += 1

    #print(ACTIVITE_EXEPTIONNELLE)
    #a dans 9 jours hihi faut faire pour le 10 par ex


def requete_marseille_traffique(path, ACTIVITE_EXEPTIONNELLE):
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
        ACTIVITE_EXEPTIONNELLE['manifestation'] += 1
    else:
        ACTIVITE_EXEPTIONNELLE['non_manifestation'] += 1

def activité_execptionnelle(lieu, ACTIVITE_EXEPTIONNELLE):


    
    if lieu == "lyon":
        path = "https://www.onlymoov.com/trafic/"
        requete_lyon_traffique(path, ACTIVITE_EXEPTIONNELLE)

        

    elif lieu == "paris":
        path = "https://paris.demosphere.net/manifestations-paris"
        requete_paris_traffique(path, ACTIVITE_EXEPTIONNELLE)

    elif lieu == "marseille":
        path = "https://mars-infos.org/spip.php?page=agenda"
        requete_marseille_traffique(path, ACTIVITE_EXEPTIONNELLE)












