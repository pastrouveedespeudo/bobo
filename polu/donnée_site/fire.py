
import requests
import urllib.request
from bs4 import *
import datetime

from CONFIG import PATH_LYON_FIRE
from CONFIG import PATH_MARSEILLE_FIRE
from CONFIG import PATH_PARIS_FIRE
from CONFIG import MONTH_DICO



def date():
    """We define the date"""
    
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    return day, month, year


def soup_lyon():
    """We searchinf fire for lyon"""
    
    day, month, year = date()
    
    path = PATH_LYON_FIRE
    request_html = requests.get(path)
    page = request_html.content
    soup_request = BeautifulSoup(page, "html.parser")
    Property = soup_request.find_all("div")

    liste = []
    liste.append(str(Property))

    daate = str(day) + ' ' + str(month) + ' ' + str(year)
    finding = str(liste).find(str(daate))

    if finding >= 0:
        return 'oui'
    else:
        return 'non'


def soup_request(path):
    """We call all div"""
    
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find_all("div")

    liste = []
    liste.append(str(Property))

    return liste


def search_date(path):
    """Here we search 
    all differents possibilities
    of format of date"""
    
    liste = soup_request(path)
    day, month, year = date()

    finding = str(liste).find('incendie')
    liste = liste[0][finding - 1000:finding + 1000]
    month_chi = month

    counter = 0
    for i in str(month_chi):
        counter += 1

    if counter == 1:
        daate1 = str(year) + '-0' + str(month_chi)+'-'+str(day)
        daate3 = str(day) + '-0' + str(month_chi)+'-'+str(year)
    else:
        daate1 = str(year) + '-' + str(month_chi)+'-'+str(day)
        daate3 = str(day) + '-' + str(month_chi)+'-'+str(year)
        
    daate = str(day) + ' ' + str(month) + ' ' + str(year)
    
    finding1 = str(liste).find(daate)
    finding2 = str(liste).find(daate1)
    finding3 = str(liste).find(daate3)

    if finding1 >= 0 or\
       finding2 >= 0 or\
       finding3 >=0:
        return 'oui'
    else:
        return 'non'

    
def fire_city(city):
    """here we are going to look for
    current fire in the three different cities."""

    path = ''
    day, month, year = date()

    for key, value in MONTH_DICO.items():    
        if str(month) == key:
            month = value

    city = city.lower()


    if city == 'lyon':
        lyon_city = soup_lyon()
        if lyon_city:
            return lyon_city

    elif city == 'paris':
        path = PATH_PARIS_FIRE
    elif city == 'marseille':
        path = PATH_MARSEILLE_FIRE


    fire = search_date(path)
    return fire









































