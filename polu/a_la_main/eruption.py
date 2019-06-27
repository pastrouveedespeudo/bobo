import requests
import urllib.request
from bs4 import *
import datetime

from CONFIG import MONTH_DICO_EN

def date():
    
    date = datetime.datetime.now()

    day = date.day
    month = date.month
    year = date.year

    month = str(month)   
    year = str(year)  

                        
    this_month = ''
    for key, value in MONTH_DICO_EN.items():
                                    
        if str(month) == key:                          
            this_month = value

            
    return day, this_month, year

def soup_search():
    
    path = "https://www.volcanodiscovery.com/fr/volcanoes/today.html"
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find_all("div", {"class":"ln"}) 
                                                    
    liste = []
    liste.append(str(Property))

    
def eruption():
    """Here we get eruption during the last week"""
        
    day, this_month, year = date()
    liste = soup_search()

    liste2 = []
    for i in range(7):      

        day = int(day)
        day = day - i
        day = str(day) 
        
        to_search = day +' '+ this_month + ' ' + year        
        to_search1 = this_month + ' ' + day + ' ' + year
        to_search2 = day + '-' + this_month + '-' +year
        to_search3 = day + '-' + this_month + '-' + year
        to_search4 = this_month + ' ' + day + ', ' + year

        finding1 = str(liste).find(str(to_search))    
        finding2 = str(liste).find(str(to_search1))
        finding3 = str(liste).find(str(to_search2))
        finding4 = str(liste).find(str(to_search3))
        finding5 = str(liste).find(str(to_search4))

        if finding1 >= 0 or\
           finding2 >= 0 or\
           finding3 >=0 or\
           finding4 >= 0 or\
           finding5 >=0: 
            day = str(day) + ' ' + this_month
            liste2.append(day)


    if liste2 != []:
        return 'oui'
    

print(eruption())


























