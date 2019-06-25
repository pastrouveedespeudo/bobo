"""This are functions for searching hairdressers
and their schedul by city input"""

import requests
from bs4 import *
import datetime

from .HAIR_CONFIG import LISTE1
from .HAIR_CONFIG import PATH_HAIRDRESSER
from .HAIR_CONFIG import PATH_SCHEDULE
from .HAIR_CONFIG import AGENT


def cities(city):
    path = PATH_HAIRDRESSER.format(city, city)

    request_html = requests.get(path)
    page = request_html.content
    
    soup_request = BeautifulSoup(page, "html.parser")
    
    Property = soup_request.find_all("span")

    liste = []

    for i in Property:
        for j in LISTE1:
            finding = str(i.string).find(str(j))
            if finding >= 0:
                liste.append(i.string)

    return liste 




def schedule_hair(name, city):

    path = PATH_SCHEDULE.format(name, city)
    
    request_html = requests.get(path, headers={"User-Agent": AGENT})
    
    page = request_html.content
    soup_request = BeautifulSoup(page, "html.parser", from_encoding="utf-8")

    Property = soup_request.find_all("td")

    liste = []
    for i in Property:
        liste.append(i.string)

    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday',]

    translate = ''
    liste1 = []
    counter = 0
    
    for i in liste:
        for j in week:
            
            finding = str(i).find(str(j))
            
            if finding >= 0:
                if i == 'Monday':
                    translate = 'lundi'
                elif i == 'Tuesday':
                    translate = 'mardi'
                elif i == 'Wednesday':
                    translate = 'mercredi'
                elif i == 'Thursday':
                    translate = 'jeudi'
                elif i == 'Friday':
                    translate = 'vendredi'
                elif i == 'Saturday':
                    translate = 'samedi'
                elif i == 'Sunday':
                    translate = 'dimanche'
                
                liste1.append([translate, liste[counter+1]])
            
        counter += 1
      
    return liste1

