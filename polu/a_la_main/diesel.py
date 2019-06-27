import requests
import urllib.request
from bs4 import *

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
        return 'dollars augmente'
    else:
       return 'dollars baisse  '
       #we let this space for visual aspect (for html page)



def soup_function():
    
    #course_dollars()
    dol = course_dollars()  

    path = "https://prixdubaril.com/" 
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")   

    propriete = soup.find_all("div", {'class':'carburant_red'})

    return propriete, dol


def finding_function():
    """Here we finding this words
    becasue we search red color
    it significate his increase"""
    
    #soup_function()
    propriete, dol = soup_function()
    
    a = str(propriete).find('Gas')
    b = str(propriete).find('Gas+')
    c = str(propriete).find('Gazole')
    d = str(propriete).find('Gazole+')


    gas = False
    gasplus = False 
    
    if a or c >= 0: 
        gas = True
    elif b or d >=0:
        gasplus = True

    return gas, gasplus, dol




def recup_tag():
    """Here we get diesel and dollars courses
    to analyze in France the sale of siesel and
    therefore the rate of diesel car right now"""

    #finding_function()
    gas, gasplus, dol = finding_function()
                                                           
    if gas == True and\
       gasplus == True and\
       dol  == 'dollars baisse  ':
        return 'tres fort'

    elif gas == True and\
         gasplus == False and\
         dol == 'dollars augmente':
        return 'moyen'

    elif gas == False and\
         gasplus == True and\
         dol == 'dollars augmente':
        return 'moyen'

    elif gas == False and\
         gasplus == False and\
         dol == 'dollars augmente':
        return 'bas'


    elif gas == True and\
         gasplus == False and\
         dol == 'dollars baisse  ':
        return 'fort'

    elif gas == False and\
         gasplus == True and\
         dol == 'dollars baisse  ':
        return 'fort'


    
    









