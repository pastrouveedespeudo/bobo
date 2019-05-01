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

from palettecouleur_coiffure import *
from coul import *
from palettecouleur import DICO_COULEUR


##        for x in range(image.shape[0]):
##            for y in range(image.shape[1]):

from colour import Color


class image_femme_haut:

    def resize(self, img, save):
       self.img = img
       self.save = save
       
       image = Image.open(self.img)


       image = image.resize((int(round(image.width/2)),
                             int(round(image.height/2))))

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

        
        diff.save("traitement_bas.jpg")

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


    def logo(self, image):
        pass


    def couleur_habit(self, image):
        self.image = image

        dico = {'bleu':0,'beige':0,'marron beige':0,'marron':0,'gris':0,
                'marron gris':0,'vert':0,'bleu clair':0,'jaune':0,'orange':0,
                'noir':0,'bleu violet':0,'beige foncé':0,'blanc':0,'kaki':0,
                'vert foncé':0,'orange foncé':0,'jaune foncé':0,'turquoise':0,
                'bleu':0,'rose':0,'rouge':0,'magenta':0}

        image = cv2.imread(self.image)
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
        print(dico)


        #print(dico)
        #cv2.imshow('image', image)








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

        print(dico)
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
            coul = couleur(i[0][0], i[0][1], i[0][2])
            if coul == None:
                pass
            else:

                if coul == 'blond':
                    dico_couleur['blond'] += 1
                    
                elif coul == 'marron':
                    dico_couleur['marron'] += 1

                elif coul == 'noir':
                    dico_couleur['noir'] += 1

                    
        print(dico_couleur)

        if dico_couleur['blond'] > dico_couleur['marron'] + 1000 and\
           dico_couleur['blond'] > dico_couleur['noir']:
            return 'blond'
            print('blond')
            
        elif dico_couleur['marron'] > dico_couleur['blond'] + 1000 and\
           dico_couleur['marron'] > dico_couleur['noir']:
            print('marron')
            return 'marron'
        
        elif dico_couleur['noir'] > dico_couleur['blond'] and\
           dico_couleur['noir'] > dico_couleur['noir']:
            print('noir')
            return 'noir'
        
        elif dico_couleur['marron'] >= dico_couleur['blond'] + 400 and\
           dico_couleur['marron'] > dico_couleur['noir']:
            print('chatin')
            return 'chatin'
            
        elif dico_couleur['blond'] >= dico_couleur['marron'] + 400 and\
           dico_couleur['blond'] > dico_couleur['noir']:
            print('chatin')
            return 'chatin'





            
    def essais(self):
        im = cv2.imread('traitement_haut.jpg')
        im[50:90,50] = 254,107,0
        cv2.imshow('image', im)
    
if __name__ == '__main__':

    
    image_femme_haut = image_femme_haut()

    

    IMAGE = '2a.jpg'
    
    #image_femme_haut.mask_bas(IMAGE)
    #image_femme_haut.mask_haut(IMAGE)
    
    image_femme_haut.resize(IMAGE_TRAITEMENT_HAUT, 'traitement_haut1.jpg')
    
    image_femme_haut.couleur_habit('traitement_haut1.jpg')
    

    
    #image_femme_haut.couleur_cheveux('6b.jpg')

    #image_femme_haut.essais()
















































