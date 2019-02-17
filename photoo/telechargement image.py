# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from path import *
import urllib.request
import json
from PIL import Image

class yo:
    def recherche_image_phrase(self, phrase):

        
        self.phrase = phrase

        liste = []
        
        
        path =  "https://www.google.co.in/search?q={0}&source=lnms&tbm=isch"
        path1 = path.format(self.phrase)
        requete = requests.get(path1)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find_all("img")
        
        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)


        for i in range(50):
            a = str(liste).find(str("src"))
            b = str(liste).find(str('" width='))
            
            url = liste[0][a+2:b-3]
            image = str("image_"+self.phrase+str(i)+".jpg")

            liste[0] = liste[0][b:-3]

            urllib.request.urlretrieve(str(url), image)

           


 

yo = yo()
yo.recherche_image_phrase("coupe de cheveux")









