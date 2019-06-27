
import requests
import datetime
import urllib.request
from bs4 import *


from .CONFIG import DEAPARTURE

def trafique_circulation():

    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute

    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""

    
    for i in DEAPARTURE:
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


def function_plugs_lyon(city):
    
    path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(city)
  
    r = requests.get(path)

    km = ''

    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find("span", {'class':'font38 green'})
    liste = []
    print(Property)

    return Property

def plugs_lyon(city):

        liste = []
        km = ''
        
        Property = function_plugs_lyon(city)
        
        for i in Property:
            for j in i:
                if j == 'K' or j == 'k':
                    km = True

        try:
            for i in Property:
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
            
        if b == 0 or\
           b == 0.0:
            return 'non'

        elif b > 0  and\
             b <= 5:
            return 'petit'

        elif b > 5 and\
             b <= 9:
            return 'moyen'

        elif b > 9 and\
             b <= 15:
            return 'grand'

        elif b > 15 and\
             b <= 20:
            return 'assez grand' 

        elif b > 20:
            return 'tres grand' 



def plugs_paris():
    
    path = "http://www.sytadin.fr/sys/barometre_courbe_cumul.jsp.html#"

    r = requests.get(path)

    liste = []

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    liste.append(str(soup))
    plug = liste[0][1870:1890]
    plug = str(plug)

    kmplug = []
    liste = []
    
    for i in plug:
        try:
            i = int(i)
            kmplug.append(str(i))
            
        except:
            pass

    kmplug = "".join(kmplug)

    try:
        kmplug = int(kmplug)
    except:
        pass
    
    b = kmplug
       
    if b == 0 or\
       b == 0.0:
        return 'non'

    elif b > 0  and\
         b <= 5:
        return 'petit'

    elif b > 5 and\
         b <= 9:
        return 'moyen'

    elif b > 9 and\
         b <= 15:
        return 'grand'

    elif b > 15 and\
         b <= 20:
        return 'assez grand' 

    elif b > 20:
        return 'tres grand' 

def bouchons(city):
    """From this site web we get plugs into this city"""
    
    if city == "lyon":
        plugs1 = plugs_lyon(city)
        return plugs1



    elif city == "paris":
        plugs2 = plugs_paris()
        return plugs2

    elif city == "marseille":
        return 'moyen'




def traffic_lyon_request(path):
    """we search demonstration Lyon"""
    
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find('div',attrs={"class":u"news"})


    trafic = str(Property).find(str("circulation"))
    trafic1 = str(Property).find(str("dense"))
    trafic2 = str(Property).find(str("très dense"))

    manif = str(Property).find(str("Manifestation"))
    manif1 = str(Property).find(str("manifestation"))

    #and return if manif there are or not
    if manif >= 0 or manif1 >=0 :
        return 'manifestation'
    else:
        return 'non_manifestation'




def traffic_paris_function_request(path):
    
    date = datetime.datetime.now()
    day = date.day
    day_week = date.weekday()

    liste = []
    r = requests.get(path)
    

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    Property = soup.find_all("table")


    for i in Property:
        date = soup.find('span',attrs={"class":u"wday"})
    
    return Property, date, day, day_week


def traffic_paris_function_reuqest1(path):
    
    Property, date, day, day_week = traffic_paris_function_request(path)
   
    date = str(date)
    the_day  = ''

    
    monday = str(date).find("lundi")
    tuesday = str(date).find("mardi")
    wednesday = str(date).find("mercredi")
    thursday = str(date).find("jeudi")
    friday = str(date).find("vendredi")
    saturday = str(date).find("samedi")
    sunday = str(date).find("dimanche")

    if monday > 0 :
        the_day = 0
    if tuesday > 0 :
        the_day = 1
    if wednesday > 0 :
        the_day = 2
    if thursday > 0 :
        the_day = 3
    if friday > 0 :
        the_day = 4
    if saturday > 0 :
        the_day = 5
    if sunday > 0 :
        the_day = 6

    numero_mois = [date]
    numero_mois = numero_mois[0][23:42]

    return numero_mois, the_day, date, day, day_week

    
def traffic_paris_request(path):
    """we search demonstration Paris"""

    numero_mois, the_day, date, day, day_week = traffic_paris_function_reuqest1(path)

    num = []
   
    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)
            
        except:
            pass

    if the_day == day_week and num[0] == day:
        return 'manifestation'
    else:
        return 'non_manifestation'
       



def traffic_marseille_request(path):
    """we search demonstration Marseille"""

    numero_mois, the_day, date, day, day_week = traffic_paris_function_reuqest1(path)

    num = []
   
    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)
            
        except:
            pass

    if the_day == day_week and num[0] == day:
        return 'manifestation'
    else:
        return 'non_manifestation'


def activité_execptionnelle(city):
    """we call the last 3 functions"""
    
    if city == "lyon":
        path = "https://www.onlymoov.com/trafic/"
        finding = traffic_lyon_request(path)

        return finding

    elif city == "paris":
        path = "https://paris.demosphere.net/manifestations-paris"
        finding = traffic_paris_request(path)

        return finding

    elif city == "marseille":
        path = "https://mars-infos.org/spip.php?page=agenda"
        finding = traffic_marseille_request(path)

        return finding












