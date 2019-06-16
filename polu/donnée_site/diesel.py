"""BS4, Request, str.find 16/04/2019"""


import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *


def recup_tag():
    """Here we get diesel and dollars courses
    to analyze in France the sale of siesel and
    therefore the rate of diesel car right now"""



    dol = course_dollars()  #we call course_dollars()
                            #because dollars // price diesel
    
    
    path = "https://prixdubaril.com/" #We take url site
    r = requests.get(path)#requests stuff
    page = r.content
    soup = BeautifulSoup(page, "html.parser")   #Soup stuff

    propriete = soup.find_all("div", {'class':'carburant_red'})
                                    #We searching this balise
    
    a = str(propriete).find('Gas')
    b = str(propriete).find('Gas+')
    c = str(propriete).find('Gazole')
    d = str(propriete).find('Gazole+')#And search this str.
                                      #if variable are found into propriete (balise)
                                      #so it return number >= 0.
    

    gas = False
    gasplus = False #Initializing gas and gasplus (diesel) to False
    
    if a or c >= 0: #If the returning number is >= 0 so it become True
        gas = True
    elif b or d >=0:
        gasplus = True


    #Now we playing with condition and return it for "our analysis"
    if gas == True and gasplus == True and dol  == 'dollard baisse  ':
        return 'tres fort'

    elif gas == True and gasplus == False and dol == 'dollard augmente':
        return 'moyen'

    elif gas == False and gasplus == True and dol == 'dollard augmente':
        return 'moyen'


    elif gas == False and gasplus == False and dol == 'dollard augmente':
        return 'bas'


    elif gas == True and gasplus == False and dol == 'dollard baisse  ':
        return 'fort'

    elif gas == False and gasplus == True and dol == 'dollard baisse  ':
        return 'fort'


    
def course_dollars():
    """Here we try to get course of dollars BeautifulSoup and Request"""
    
    path = "https://prixdubaril.com/"

    r = requests.get(path)

    page = r.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("span")


    liste = []
    liste.append(str(propriete))


    dollar = liste[0][520:525]
    
    if dollar[0] == '+':
        return 'dollard augmente'
    else:
       return 'dollard baisse  '










