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
import psycopg2




class image_femme_haut:

    def resize(self, img, save):
       self.img = img
       self.save = save
       
       image = Image.open(self.img)

       image = image.resize((30,30))
                            
       image.save(self.save)

       
    def mask_bas(self, i):
        self.i = i

        print('mask bas de :', self.i)

        
        img = Image.open(self.i)
   
        masque = Image.new('RGB', img.size, color=(255,255,255))

        a = img.size[0] / 100 *30
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

        print('mask haut de :', self.i)

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

        print(self.image, ' : en cours')

        image = cv2.imread(self.image)

        largeur = image.shape[1]
        hauteur = image.shape[0]

        taille = largeur * hauteur
        
        couleur_liste = []
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                
                colordb = get_colordb('bobo.txt')
                if not colordb:
                    print('No parseable color database found')
                    sys.exit(1)
                nearest = colordb.nearest(image[x,y][2],
                                          image[x,y][1],
                                          image[x,y][0])
    
                couleur_liste.append(nearest)

        print(couleur_liste)
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
            print('couleur de cheveux blond')
            return 'blond'
            
            
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
 

    def traitement(self):
        
 
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\photo\analysis\image_femme')
        liste = os.listdir()

        for i in liste:
            
            if i == '__pycache__' or i == 'analyse_femme_haut.py' or\
               i == 'constante.py' or i == 'coul.py' or\
               i == 'palettecouleur.py' or i == 'palettecouleur_coiffure.py' or\
               i=='bobo.txt' or i== 'traitement_haut.jpg' or i == "traitement_bas1.jpg" or\
               i == 'config.py' or i == 'constante.py' or i =='coul.py' or i == 'database.py' or\
               i == 'palettecouleur.py' or i =='palettecouleur_coiffure.py':
                pass
            
            else:
                nom = i[-5:-4]

                
                if nom == 'a':
                    pass
##                    image_femme_haut.mask_bas(i)
##                    
##                    image_femme_haut.resize('traitement_haut.jpg', 'traitement_haut.jpg')
##                    haut = image_femme_haut.couleur_habit('traitement_haut.jpg')
##                    
##                         
##                    image_femme_haut.mask_haut(i)
##                    
##                    image_femme_haut.resize('traitement_bas1.jpg', 'traitement_bas1.jpg')
##                    bas = image_femme_haut.couleur_habit('traitement_bas1.jpg')
##
##                    insertion_table.insertion_info(self,
##                                                   i,
##                                                   'féminin',
##                                                   haut[1],
##                                                   bas[1],
##                                                   haut[0],
##                                                   bas[0])


                elif nom == 'b':
                
                    coiffure = image_femme_haut.couleur_cheveux(i)
                    print(coiffure)
                    insertion_table.coiffure(self, i,
                                             coiffure)
                                             
                    





if __name__ == '__main__':

    image_femme_haut = image_femme_haut()
    image_femme_haut.traitement()

        
















































