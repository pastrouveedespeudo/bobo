"""Bs4, request, str find 16/04/2019"""

import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
import datetime

#This is path of fire to the differents cities
PATH_LYON = 'https://www.lyoncapitale.fr/?s=incendie'
PATH_MARSEILLE = 'https://www.20minutes.fr/search?q=incendie+marseille'
PATH_PARIS = 'https://www.20minutes.fr/search?q=incendie+paris'


def fire_city(city):
    """here we are going to look for
    current fire in the three different cities."""

    
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    dico = {'1':'janvier','2':'fevrier','3':'mars','4':'avril',
            '5':'mai','6':'juin','7':'juillet','8':'août',
            '9':'septembre','10':'octobre','11':'novembre','12':'decembre'}#We define current time
                                                                           #for search current fire.

    #we search the dictionary to find the current month
    for key, value in dico.items():    
        if str(month) == key:
            month = value

    city = city.lower()

    #If city is Lyon, we recup all div from the html page.
    if city == 'lyon':
        path = PATH_LYON
        r = requests.get(path)
        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        Property = soup.find_all("div")

        #we put the result of the search in a list
        liste = []
        liste.append(str(Property))

        #And search the current date.
        daate = str(day) + ' ' + str(month) + ' ' + str(year)
        a = str(liste).find(str(daate))

        #If a >= 0 this only fire page have an article fire to lyon today
        if a >= 0:
            return 'oui'



    #we use a similar technique that Lyon technique
    elif city == 'paris':
        path = PATH_PARIS
    elif city == 'marseille':
        path = PATH_MARSEILLE
    
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find_all("div")

    liste = []
    liste.append(str(Property))

    a = str(liste).find('incendie')

    liste = liste[0][a-1000:a+1000]

    month_chi = date.month

    c = 0
    for i in str(month_chi):
        c+=1

    if c == 1:
        daate1 = str(year) + '-0' + str(month_chi)+'-'+str(day)
        daate3 = str(day) + '-0' + str(month_chi)+'-'+str(year)
    else:
        daate1 = str(year) + '-' + str(month_chi)+'-'+str(day)
        daate3 = str(day) + '-' + str(month_chi)+'-'+str(year)
        
    daate = str(day) + ' ' + str(month) + ' ' + str(year)
    
    b = str(liste).find(daate)
    c = str(liste).find(daate1)
    d = str(liste).find(daate3)

    if b >= 0 or c >= 0 or d >=0:
        return 'oui'
    


fire_city("marseille")






































