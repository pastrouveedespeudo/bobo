import requests
from bs4 import BeautifulSoup
import urllib.request
import json
from PIL import Image, ImageDraw, ImageChops
import os
import cv2




LISTE = ["femme","fille","homme","garcon"]#sert au telechargement d'image

LISTE_SEXE_HOMME = ["homme", "gacon"] #sert pour les poids
LISTE_SEXE_FEMME = ["femme","fille"]

DEPART = ["bleu", "bleu"]

FINAL = []

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



    def mask_haut(self, i):#ICI on peut faire rafractionnre ou mélanger mais bon...
                        #chui en retard et la barbe
        

        
        img = Image.open(str(i))
        print(i)
        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[1] 
        b = img.size[0] / 100 * 60

        c = 0
        d = 0

        coords = (a,b, c,d)
   
        
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)

        diff.save("traitement_haut.jpg")
        

    def mask_bas(self, i):
        

        img = Image.open(str(i))
        print(i)
        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[0]
        b = img.size[1] / 100* 60
        c = 0
        d = img.size[1]

        coords = (a,b, c,d)
   
        
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)

        diff.save("traitement_bas.jpg")
        FINAL.append(i)

    def couleur(self, image):
        
        self.im = Image.open(image)


        liste = []
        
        dico = {}
        for value in self.im.getdata():
            if value in dico.keys():
                 dico[value] += 1
            else:
                 dico[value] = 1


        liste_dico = []
        for i in dico.values():
            liste_dico.append(i)
            
        liste_dico= sorted(liste_dico, reverse = True)

        for i in liste_dico:
            liste.append([c for c,v in dico.items() if v==i])
            if i <= 5:
                break


        liste_finale = []
        for i in liste:
            for j in i:
                
                if j[0] == j[1] == j[2]:
                    pass
                elif j[0] <= j[1] + 10 and j[0] >= j[1]-10  and\
                     j[0] <= j[2] + 10 and j[0] >= j[2]-10:
                    pass 


                
                else:
                    liste_finale.append(j)


        FINAL.append(liste_finale)




    def sexe(self, liste):

        self.liste = liste
 
        DICTIONNAIRE = {}
        LISTE_HOMME = []
        LISTE_FEMME = []
        
        liste = os.listdir()
  
        for i in liste:     #on "initialise les poids" 
            if i == "requete.py" or i == "tendance.py"\
               or i == "haarcascades_haarcascade_lowerbody"\
               or i == "essais.py":
                pass
            else:
                DICTIONNAIRE[i] = 0

        a = 0
        for i in liste:    #si y'a homme ou garcon dans le titre alors +1
            for image in self.liste:
                
                sexe = str(i).find(str(image))

                if sexe >= 0:
                   
                    DICTIONNAIRE[i] += 1
           

        #print(DICTIONNAIRE)
        FINAL.append(liste)#sauf que ya difference entre homme et garcon...
        FINAL.append("   ")




#ok le but c de lui faire 











#1 on telecharge les images
#2 on parcours la liste des images et on ignore les fichier py
#3 on fais un mask de l'image en haut et en bas
#4 on fait des pts sur le haut et le bas de facon a etre sur que c sur le vetement
#5 on récupere les couleurs et on stock ca  et on regarde les deux couleurs a chaque fois
        #dapres tous les pts on regarde si ca depasse pas a chaque fois du seil
        #au moins x des valeurs

        #on aura les valeurs sous formes de bvr








        
# on regarde dans le titre si on trouve mec ou fille
# on commence les poids du sexe des hommes



if __name__ == "__main__":

    
    yo = tendance()



    liste = os.listdir()

    for i in liste: 
        if i == "requete.py" or i == "tendance.py"\
           or i == "essais.py":
            pass
        else:
            #yo.internet()

            yo.mask_haut(i)
            yo.mask_bas(i)

            yo.couleur("traitement_haut.jpg")
            yo.couleur("traitement_bas.jpg")


            yo.sexe(LISTE_SEXE_HOMME)














