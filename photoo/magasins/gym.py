"""This is functions for search gym area from bs4"""
import requests
from bs4 import *


from .GYM_CONFIG import GYM
from .GYM_CONFIG import PATH_CITY
from .GYM_CONFIG import AGENT
from .GYM_CONFIG import PATH_SCHEDULE


def big_city_gym(city):
    """Here we search gym into the cities"""

    path = PATH_CITY.format(city)
    request_html = requests.get(path)
    page = request_html.content

    var_soup = BeautifulSoup(page, "html.parser")

    propriete = var_soup.find_all("span")
    liste1 = []

    for i in propriete:
        for j in GYM:
            var_find = str(i.string).find(str(j))
            if var_find >= 0:
                liste1.append(i.string)

    return liste1


def schedule_gym(name, city):
    """We search all schedule from gym found"""

    path = PATH_SCHEDULE.format(name, city)

    request_html = requests.get(path, headers={"User-Agent": AGENT})

    page = request_html.content
    soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")

    #propriete = soup.find_all("span")
    propriete = soup.find_all("td")

    liste = []
    for i in propriete:
        liste.append(i.string)


    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday',]


    liste1 = []
    count = 0
    
    for i in liste:
 
        for j in week:
            var_find = str(i).find(str(j))
            if var_find >= 0:
                liste1.append([i, liste[c+1]])

        count += 1


    return liste1
