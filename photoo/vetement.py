import os
import cv2
from PIL import Image



#chignon = {"haut":"t-shirt rouge", "bas":"jean bleu"}
#LISTE = [chignon]
CHIGNON = ["t-shirt rouge", "jean bleu"]
NOIR = [255, 255, 255]
BLEU = [0,0,255]

TRAITEMENT = []
POIDS = 0
VETEMENT = {}

DICTIONNAIRE = {}

#ici vetement selon la coupe
#selon le site

#faudra ajuster les para ex: chignon ou frange

def ajustage_couleur(image):#ici faudra faire genre si tu veux du vert l'ajuster

    ok = "BLEU"
    pas_ok = "PAS BLUWW"

    liste = []
    im = cv2.imread(str(image))

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):

            if im[x,y][1] <= 80 and im[x,y][1] >= 0\
               and im[x,y][2] >= 40 and im[x,y][2] <= 120\
               and im[x,y][0] > [x,y][1] + 40 and im[x,y][0]> im[x,y][2] + 40:
               
                liste.append("ok")

    if liste != [ ]:
        return ok
    else:
        return pas_ok
        
    
    #ne marche que pour le bleu et les autre peut etre
      #0     0    255
      #86     140  187
    

def ajustage_couleur_2(image, couleur, vertmin, vermax, rougemin, rougemax):

    ok = couleur
    pas_ok = "NOPE"

    liste = []
    im = cv2.imread(str(image))

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):

            if im[x,y][1] <= vertmin and im[x,y][1] >= vermax\
               and im[x,y][2] >= rougemin and im[x,y][2] <= rougemax\
               and im[x,y][0] > [x,y][1] + 40 and im[x,y][0]> im[x,y][2] + 40:
               
                liste.append("ok")
    if liste != [ ]:
        return ok
    else:
        return pas_ok
    


class vetement:

    def reinitialisation(self):
        POIDS = 0
        DICTIONNAIRE = {}
        
    def search_data(self):
        pass


    def search_couleur(self):#ici faudra mettre le type de vetement genre pull et ca va dans le dossier pull

        os.chdir(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\vetement\pantalon")
        liste = os.listdir()
        
        for i in liste:
            DICTIONNAIRE[i] = 0

        
        for i in liste:

            ajustage = ajustage_couleur(i)
       
            if ajustage == "BLEU":
            
                #normalement ici on met genre pas bleu mais un autre truk
                DICTIONNAIRE[i] += 1
                
            elif ajustage != "BLEU":
           
                DICTIONNAIRE[i] -= 1

                
        print(DICTIONNAIRE)
 
    #1/-1/0

    def search_sexe(self):
        pass
    #-1 non 1 oui f=f 0 je sais pas

    def haut_bas(self):
        pass












    #enfete ici on aura une catégorie tshirt et pull donc...




    #comment reconnaitre un tshirt d'un pull?
    #forme pts image
    #on montre un fois on fait les poids
    #et sur 20 essais on lui fais apprendre ok


    
    #tshit tshirt manghe longue == skin detector oki
    #short//pantalon ok
    #shot//bermuda ok




    def choix(self):
        pass
    #ici affiche tous les max liste




    def ajout(self):
        pass
    #if + de 3 images chignon == t-shit+bermuda LISTE.append et du coup on doit
    #reco



yo = vetement()
yo.search_couleur()










        
