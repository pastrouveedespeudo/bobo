"""BS4, Requests, DateTime, Str.Find 16/04/2019"""

import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *



def eruption():
    """Here we get eruption during the last week"""
        
    date = datetime.datetime.now()

    month = date.month
    year = date.year

    month = str(month)   #-> We get time of the current day. 
    year = str(year)  #and tranform it to str stuff.
                        

                        #because we'ill compare it to this dico.
    dico = {'1':'January', '2':'February', '3':'March','4':'April','5':'May','6':'June',
            '7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

    this_month = ''
    for key, value in dico.items():#We trying to search the current month and attribute it 
                                    #to variable this_month,
        if str(month) == key:        #By a for loop. Thank to that we can
                                    #search eruption from this week from this month.
            this_month = value


    path = "https://www.volcanodiscovery.com/fr/volcanoes/today.html"
    r = requests.get(path)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    Property = soup.find_all("div", {"class":"ln"}) #we are looking for this tag
                                                     #and attribute container of it to a list 
    liste = []
    liste.append(str(Property))


    liste2 = []
    for i in range(7):      #7 times for a week we searching the last seven days on this site web and return
                            #yes for eruption if list isn't empty.

        day = date.day
        day = str(day-i) #for example: today : 8/06 for 7times we doing: 8-n-1.
        
        #Here are the date schema possibilities of this site.
        to_search = day +' '+ this_month + ' ' + year        
        to_search1 = this_month + ' ' + day + ' ' + year
        to_search2 = day + '-' + month + '-' +year
        to_search3 = day + '-' + this_month + '-' + year
        to_search4 = this_month + ' ' + day + ', ' + year

        a = str(liste).find(str(to_search))    #if this schem is present it return >= 0.
        b = str(liste).find(str(to_search1))
        c = str(liste).find(str(to_search2))
        d = str(liste).find(str(to_search3))
        e = str(liste).find(str(to_search4))

        if a >= 0 or b >= 0 or c >=0 or d >= 0 or e >=0: #If >= 0 We append it to a list.
            day = str(day) + ' ' + month
            liste2.append(day)


    if liste2 != []:
        return 'oui'#yes for erupt.
    

    


























