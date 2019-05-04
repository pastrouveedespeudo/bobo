import sys
import os
import cv2
from colour import Color
import numpy as np
from PIL import Image, ImageDraw, ImageChops
from matplotlib import pyplot as plt
import math

from constante import HAAR_FACE
from constante import HAAR_YEUX
from constante import IMAGE_TRAITEMENT_HAUT
from constante import IMAGE_TRAITEMENT_BAS

from palettecouleur_coiffure import couleur_cheuvelure
from coul import *
from palettecouleur import DICO_COULEUR

from colour import Color

from database import insertion_table





class image_femme_haut:

    def resize(self, img, save):
       self.img = img
       self.save = save
       
       image = Image.open(self.img)

       image = image.resize((50,50))
                            
       image.save(self.save)

       
    def mask_bas(self, i):
        self.i = i
        img = Image.open(self.i)
   
        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[0]
        b = img.size[1] / 100* 70
        c = 0
        d = img.size[1]

        coords = (a,b, c,d)
   
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)

        img = img.rotate(180)
        img.crop((0, 0, b/2, a)).save('traitement_bas1.jpg')

    def mask_haut(self, i):
        self.i = i
        img = Image.open(self.i)

        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[1]
        b = img.size[0] / 100 * 100
       
        c = 0
        d = 0

        coords = (a,b, c,d)
   
        
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)
  
 
        img.crop((0, 0, b, a/2)).save('traitement_haut.jpg')



    def couleur_habit(self, image):
        self.image = image

        dico = {'bleu':0,'beige':0,'marron beige':0,'marron':0,'gris':0,
                'marron gris':0,'vert':0,'bleu clair':0,'jaune':0,'orange':0,
                'noir':0,'bleu violet':0,'beige foncé':0,'blanc':0,'kaki':0,
                'vert foncé':0,'orange foncé':0,'jaune foncé':0,'turquoise':0,
                'bleu':0,'rose':0,'rouge':0,'magenta':0}
        

        image = cv2.imread(self.image)

        largeur = image.shape[1]
        hauteur = image.shape[0]

        taille = largeur * hauteur
        
        
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                
                colordb = get_colordb('bobo.txt')
                if not colordb:
                    print('No parseable color database found')
                    sys.exit(1)
                nearest = colordb.nearest(image[x,y][2],
                                          image[x,y][1],
                                          image[x,y][0])
    
                for clé, valeur in DICO_COULEUR.items():
                    if nearest == clé:
                        for clé1, valeur1 in dico.items():
                            if clé1 == DICO_COULEUR[nearest]:
                                dico[clé1] += 1

        couleur_liste = []
                                
        for cle, valeur in dico.items():
            if valeur != 0:
                couleur_liste.append((cle, valeur))


        return taille, couleur_liste
        


    def couleur_cheveux(self, image):
        self.image = image

        dico = {}
        dico_couleur = {'marron':0,
                        'noir':0,
                        'blond':0}

        im = Image.open(self.image)
        for value in im.getdata(): 
             if value in dico.keys():
                 dico[value] += 1
             else:
                 dico[value] = 1

   
        liste = []
        
        for cle, valeur in dico.items():
            liste.append((cle, valeur))
                
        liste2 = []
        for i in liste:
            if i[0][0] >= 240 and\
               i[0][1] >= 240 and\
               i[0][2] >= 240:
                pass
            else:
                liste2.append(i)

        for i in liste2:
            coul = couleur_cheuvelure(i[0][0], i[0][1], i[0][2])
            if coul == None:
                pass
            else:

                if coul == 'blond':
                    dico_couleur['blond'] += 1
                    
                elif coul == 'marron':
                    dico_couleur['marron'] += 1

                elif coul == 'noir':
                    dico_couleur['noir'] += 1

                    


        if dico_couleur['blond'] > dico_couleur['marron'] + 1000 and\
           dico_couleur['blond'] > dico_couleur['noir']:
            return 'blond'
            print('couleur de cheveux blond')
            
        elif dico_couleur['marron'] > dico_couleur['blond'] + 1000 and\
           dico_couleur['marron'] > dico_couleur['noir']:
            print('couleur de cheveux marron')
            return 'marron'
        
        elif dico_couleur['noir'] > dico_couleur['blond'] and\
           dico_couleur['noir'] > dico_couleur['noir']:
            print('couleur de cheveux noir')
            return 'noir'
        
        elif dico_couleur['marron'] >= dico_couleur['blond'] + 400 and\
           dico_couleur['marron'] > dico_couleur['noir']:
            print('couleur de cheveux chatin')
            return 'chatin'
            
        elif dico_couleur['blond'] >= dico_couleur['marron'] + 400 and\
           dico_couleur['blond'] > dico_couleur['noir']:
            print('couleur de cheveux chatin')
            return 'chatin'


    def traitement(self, i):
        
        print(i)
        IMAGE = i
        if i[-5] == "a":

            image_femme_haut.mask_bas(IMAGE)
            image_femme_haut.mask_haut(IMAGE)
            
            image_femme_haut.resize(IMAGE_TRAITEMENT_HAUT,
                                    'traitement_haut1.jpg')

            image_femme_haut.resize(IMAGE_TRAITEMENT_HAUT,
                    'traitement_bas1.jpg')


            haut = image_femme_haut.couleur_habit('traitement_haut1.jpg')
            
            bas = image_femme_haut.couleur_habit('traitement_bas1.jpg')

            nom_image = str(i[0] + i[-4:])
            
            insertion_table.insertion_info(self, nom_image, "femme", str(haut[1]), str(bas[1]), haut[0], bas[0])

        elif i[-5] == "b":
            nom_image = str(i[0] + i[-4:])
            coiffure = image_femme_haut.couleur_cheveux(i)#mettre dans talbe direct
            insertion_table.coiffure(self, coiffure, nom_image)

        else:
            pass


     
if __name__ == '__main__':

    
    image_femme_haut = image_femme_haut()

    liste = os.listdir()

    for i in liste:
        if i == '__pycache__' or i == 'analyse_femme_haut.py' or\
           i == 'constante.py' or i == 'coul.py' or\
           i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py':
            pass
        else:

            image_femme_haut.traitement(i)

                

        
















































