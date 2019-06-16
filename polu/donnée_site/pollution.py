import requests
import urllib.request
from bs4 import *
import datetime


CLE = '5a72ceae1feda40543d5844b2e04a205'


def particle_rate(city):
    """we search particule rate"""
    
    liste = []
    nb = []

    #Using BS4
    path = "https://air.plumelabs.com/fr/live/{}".format(city)
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("div", {'class':'report__pi-number'})

    #Get text from html page
    for i in propriete:
        liste.append(i.get_text())

    #Get the number of pollute
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


def pressure_city(city):
    """we search pressure"""

    #Call API openweathermap
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(city,CLE)
    r = requests.get(localisation)
    data=r.json()

    #get from json content
    pressure = data['main']['pressure']
    return pressure


def weather_city(city, data_ask):
    """we search weather"""

    #Call API openweathermap
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(city,CLE)
    r = requests.get(localisation)
    data=r.json()

    #get from json content
    if data_ask == 'vent':
        wind = data['wind']['speed']
        return wind
    
    elif data_ask == 'météo':
        weather = data['weather'][0]['main']

        data = ''

        #Translate it to fr
        if weather == 'Clouds' or weather == 'Mist':
            data = 'Nuageux'
        elif weather == 'Rain' or weather == 'Thunderstorm'\
             or weather == 'Haze':
            data = 'Pluie'
        elif weather == 'Clear':
            data = 'Beau temps'

        
        return data

def climate_city(city):
    """we search climate"""

    #Call API openweathermap
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}".format(city,CLE)
    r = requests.get(localisation)
    data=r.json()

    #get json stuff
    temperature = data['main']['temp']
    temperature = temperature - 273.15

    return temperature

        
def season():
    """we search season"""

    #Get the current time
    date = datetime.datetime.now()
    month = date.month
    day = date.day

    #translate it
    if month == 12 or month == 1\
       or month == 2:
        return 'hiver'

    elif month == 3 or month == 4\
         or month == 5:
        return 'primtemps'

    elif month == 6 or month == 7\
         or month == 8\
         or month == 9:
        return 'été'

    elif month == 10 or month == 11\
         or month == 12:
        return 'automne'


def traffic(city):
    """we search traffic"""

    #Get the departure thank for bison futé
    #and get hours points.
    date = datetime.datetime.now()
    
    day = date.day
    month = date.month
    year = date.year

    hour = date.hour
    minute = date.minute

    hour = hour + 2

    hour_point_week = [7,8,9,16,17,18,19]

    deaparture = [(2,1), (5,1), (9,2), (16,2), (22,2),(23,2),
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
    point = ""
    normal = ""
    no_point = ""

    #if matching departure == yes
    for i in deaparture:
        if (day, month) == i :
            dep = 'Oui'

        elif (day, month) != i :
            normal = 'Oui'
            dep = 'Non'
            

    for i in hour_point_week:

        if i == hour:
            point = 'Oui'
            no_point = 'Non'
            break

    #if matching point == yes
    if point == '':
        point = 'Non'
        no_point = 'Oui'



    return dep, point, normal, no_point



def habit():
    """we search habit"""
    
    weekend = ''
    day_of_week = ''

    #Weekend or day week
    point = [8,9,16,17,18,19]
    day = ['samedi', 'dimanche']

    
    date = datetime.datetime.now()

    hour = date.hour
    day = date.weekday()
   
   

    if day == 5 or day == 6:
        weekend = 'Weekend'
        day_of_week = 'Non'
        
    else:
        weekend = 'Non'
        day_of_week = 'Oui'

    return weekend, day_of_week



def city_ranking_pollute(lieu):
    """we search ranking pollute Fr"""
    
    liste = ["paris", "marseille", "grenoble", "mulhouse",
             "marignane","strasbourg","lyon"]

    for i in liste:
        if lieu == i:
            indexing = liste.index(i)
    
    
    return indexing + 1



def industrial_area(city):
    """we search industrial area Fr"""

    site = ''
    
    polluting_pole = ['Nord',
                    'Bouches-du-Rhône',
                    'Moselle',
                    'Seine-Maritime',
                    'Loire-Atlantique',
                    'Haute-Normandie',
                    'Meurthe-et-Moselle',
                    'Seine-Maritime',
                    'Rhône'
                    ]

    #BS4 stuff
    path = "https://fr.wikipedia.org/wiki/{}".format(city) 
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find('table',attrs={"class":u"infobox_v2"})
    Property = str(Property)
   
    #If city matching with polluting_pole we return yes
    for i in polluting_pole:
        a = str(Property).find(str(i))
        if a > 0:
            site = 'oui'
            return site

    site = 'non'
    return site




def traffic_lyon_request(path):
    """we search demonstration Lyon"""
    
    liste = []
    #We searching a tag from html page
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find('div',attrs={"class":u"news"})

    #We trying to find this words for the circulation
    trafic = str(Property).find(str("circulation"))
    trafic1 = str(Property).find(str("dense"))
    trafic2 = str(Property).find(str("très dense"))


    #We trying to find this words for demonstration
    manif = str(Property).find(str("Manifestation"))
    manif1 = str(Property).find(str("manifestation"))

    #and return if manif there are or not
    if manif >= 0 or manif1 >=0 :
        return 'il y a une manifestation'
    else:
        return 'non pas manifestation'

    news = [str(Property)]
    number = news[0][160:165]
    number2 = []
    for i in number:
        
        try:
            i = int(i)
            number2.append(i)

        except:
            pass

    
def traffic_paris_request(path):
    """we search demonstration Paris"""

    
    semaine = {'lundi':0, 'mardi':1, 'mercredi':2, 'jeudi':3, 'vendredi':4, 'samedi':5,
               'dimanche':6}

    liste = [[],[]]

    #We using bs4
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
    


    date = str(date)

    #from this site we searching demonstration during the week
    monday = str(date).find("lundi")
    tuesday = str(date).find("mardi")
    wednesday = str(date).find("mercredi")
    thursday = str(date).find("jeudi")
    friday = str(date).find("vendredi")
    saturday = str(date).find("samedi")
    sunday = str(date).find("dimanche")

    #we recup into variable demonstrations
    if monday > 0 :
        a = 0
    if tuesday > 0 :
        a = 1
    if wednesday > 0 :
        a = 2
    if thursday > 0 :
        a = 3
    if friday > 0 :
        a = 4
    if saturday > 0 :
        a = 5
    if sunday > 0 :
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

    
    #We matching current day and demonstration on agenda and
    #return it
    if a == day_week and num[0] == day:
        return 'il y a une manifestation'
    else:
        return 'non pas manifestation'
       



def traffic_marseille_request(path):
    """we search demonstration Marseille"""

    #Same techic cf  traffic_paris_request
    r = requests.get(path)

    date = datetime.datetime.now()
    jour = date.day
    jour_semaine = date.weekday()
    
    
    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    date = soup.find('div',attrs={"class":u"ml-agenda-date-page"})
   
    date = str(date)
    
    a = 0
    monday = str(date).find("lundi")
    tuesday = str(date).find("mardi")
    wednesday = str(date).find("mercredi")
    thursday = str(date).find("jeudi")
    friday = str(date).find("vendredi")
    saturday = str(date).find("samedi")
    sunday = str(date).find("dimanche")
    
    if monday > 0 :
        a = 0
    if tuesday > 0 :
        a = 1
    if wednesday > 0 :
        a = 2
    if thursday > 0 :
        a = 3
    if friday > 0 :
        a = 4
    if saturday > 0 :
        a = 5
    if sunday > 0 :
        a = 6


    number = soup.find('div',attrs={"class":u"ml-agenda-date-page"})
    #print(numero)
    number = str(number)
    number = number[20:]
    
    try:
        number = int(number)
    except:
        liste = []
        number = str(number)

        for i in number:
            try:
                i = int(i)
                liste.append(i)
            except:
                pass
    #print(a)
    if a == day_week and liste[0] == day:
        return 'il y a une manifestation'
    else:
        return 'non pas manifestation'


def exceptional_activity(city):
    """we call the last 3 functions"""
    
    if city == "lyon":
        path = "https://www.onlymoov.com/trafic/"
        a = traffic_lyon_request(path)

        return a

    elif city == "paris":
        path = "https://paris.demosphere.net/manifestations-paris"
        a = traffic_paris_request(path)

        return a

    elif city == "marseille":
        path = "https://mars-infos.org/spip.php?page=agenda"
        a = traffic_marseille_request(path)

        return a



def socio(city):
    """Here we pre-define
    active pop from this cities"""
    
    lyon = 328469
    paris = 1350800 
    marseille = 762480 

    if city == 'lyon':
        return lyon

    if city == 'paris':
        return paris

    if city == 'marseille':
        return marseille
    



def plugs(city):
    """From this site web we get plugs into this city"""
    
    if city == "lyon":
        path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(city)
      
        r = requests.get(path)

        km = ''

        #BS4 Stuff
        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        Property = soup.find("span", {'class':'font38 green'})
        liste = []
        print(Property)

        #Into this tag we searching
        #str who K is present for Km
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

            #If we have found this Km
            #We trying to translate str to float for
            #plugs
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
            
        if km != True:
            b = 0
            
        return b



    #Same technic cf Lyon
    elif city == "paris":
    
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
           
        return b




