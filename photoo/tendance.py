import requests
from bs4 import BeautifulSoup
import urllib.request
import json
from PIL import Image
import os

LISTE = ["femme","fille","homme","garcon"]

DEPART = ["bleu", "bleu"]

class tendance:

    def internet(self):

        
        for image in LISTE:
            path ="https://www.google.fr/search?biw=1068&bih=515&tbm=isch&sa=1&ei=uvJvXNHMJ5S61fAPp_GziAM&q=vetement+{0}&oq=vetement+{0}&gs_l=img.3..0l5j0i67j0l4.5993.7952..8027...0.0..0.106.1244.11j2......1....1..gws-wiz-img.....0..35i39.QHxhKIYs0B8"
            recherche = path.format(image)
   
            liste = []
      
            requete = requests.get(recherche)
            page = requete.content
            soup = BeautifulSoup(page, "html.parser")  
            propriete = soup.find_all("img")
            
            with open("requete.py", "w") as file:
                file.write(str(propriete))
                        
            with open("requete.py", "r") as file2:
                b = file2.read()
            liste.append(b)


            for i in range(100):
               
                try:
                    a = str(liste).find(str("src"))
                    b = str(liste).find(str('" width='))
                    
                    url = liste[0][a+2:b-3]
                    image = str("image"+str(image)+str(i)+".jpg")

                    liste[0] = liste[0][b:-3]

                    urllib.request.urlretrieve(str(url), image)
                except:
                    pass

yo = tendance()
yo.internet()
