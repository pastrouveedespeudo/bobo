import os
import cv2
import json
import pyglet
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops

REGION_INDUSTRIEL_POLLUEE = {'oui':0,
                             'non':0,
}

PARTICULE = {'0_20':0,
            '21_40':0,
            '41_60':0,
            '61_80':0,
            '81_100':0,
            '101_120':0,
            '121_140':0,
            '141_160':0,
            '161_180':0,
            '181_200':0,
            '>200':0
}


VILLE_POLLUE2018 = {'VILLE_POLLUE2018':0,
                    'un':0,
                    'deux':0,
                    'trois':0,
                    'quattre':0,
                    'non':0,
}

REGION_INDUSTRIEL_POLLUEE = {'oui':0,
                             'non':0,
}

class particule:

    def particule(self, lieu):
        self.lieu = lieu

        liste = []
        nb = []

        path = "https://air.plumelabs.com/fr/live/{}".format(self.lieu)

        r = requests.get(path)


        page = r.content
        soup = BeautifulSoup(page, "html.parser")
    
        propriete = soup.find_all("div", {'class':'report__pi-number'})
        for i in propriete:
            liste.append(i.get_text())
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

        phrase_clé = "a atteint un niveau élevé de pollution. Supérieur à la limite maximum pour 24h établie par l'OMS"

        polution = nb
        print(polution)
        #polution = int(polution)
        

        if polution <= 20:
            PARTICULE['0_20'] += 1

        elif polution >=21 and polution <= 40:
            PARTICULE['21_40'] += 1
            
        elif polution >=41 and polution <= 60:
            PARTICULE['41_60'] += 1
            
        elif polution >=61 and polution <= 80:
            PARTICULE['61_80'] += 1
            
        elif polution >=81 and polution <= 100:
            PARTICULE['81_100'] += 1
            
        elif polution >=101 and polution <= 120:
            PARTICULE['101_120'] += 1
            
        elif polution >=121 and polution <= 140:
            PARTICULE['121_140'] += 1
            
        elif polution >=141 and polution <= 160:
            PARTICULE['141_160'] += 1
            
        elif polution >=161 and polution <= 180:
            PARTICULE['161_180'] += 1
            
        elif polution >=181 and polution <= 200:
            PARTICULE['181_200'] += 1
            
        elif polution >200:
            PARTICULE['>200'] += 1


    def france(self, lieu):
        self.lieu = lieu
  
        liste = ["lyon", "marseille","paris","roubaix"]


        c = 0
        for i in liste:

            if self.lieu == liste[0]:
                VILLE_POLLUE2018['un'] += 1
                break

            elif self.lieu == liste[1]:
                VILLE_POLLUE2018['deux'] += 1
                break

            elif self.lieu == liste[2]:
                VILLE_POLLUE2018['trois'] += 1
                break

            elif self.lieu == liste[3]:
                VILLE_POLLUE2018['quattre'] += 1
                break
            else:
                VILLE_POLLUE2018['non'] += 1
                break
                

                
            c+=1
        


    def industrie(self, lieu):
        self.lieu = lieu


        path = "https://fr.wikipedia.org/wiki/{}".format(self.lieu) 

        r = requests.get(path)

        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        propriete = soup.find('table',attrs={"class":u"infobox_v2"})
        propriete = str(propriete)

        try:
            code_postal = propriete[5649:5654]
            code_postal = int(code_postal)
            
        except:
            pass

        liste = []

        path = "http://www.cartesfrance.fr/recherche/?q={}".format(code_postal)

        r = requests.get(path)

        page = r.content
        soup = BeautifulSoup(page, "html.parser")
        
        propriete = soup.find_all('Département')




        pole_poluant = {'1':'Nord',
                        '2':'Bouches-du-Rhône',
                        '3':'Moselle',
                        '4':'Seine-Maritime',
                        '5':'Loire-Atlantique',
                        '6':'Haute-Normandie',
                        '7':'Meurthe-et-Moselle',
                        '8':'Seine-Maritime',
                        '9':'Rhône'

                        }


        for i in pole_poluant.keys():
            a = str(soup).find(str(pole_poluant[i]))
        #    print(a,pole_poluant[i])

        if a > 0:
            REGION_INDUSTRIEL_POLLUEE['oui'] += 1

        else:
            REGION_INDUSTRIEL_POLLUEE['non'] += 1
            



particule = particule()
particule.particule('paris')
particule.france('paris')
particule.industrie('paris')


print(VILLE_POLLUE2018,
    REGION_INDUSTRIEL_POLLUEE,
    REGION_INDUSTRIEL_POLLUEE,
    PARTICULE)










