import sys
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageChops
from matplotlib import pyplot as plt
import math

from constante import HAAR_FACE
from constante import HAAR_YEUX

from palettecouleur import *

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
        b = img.size[0] / 100 * 130

        c = 0
        d = 0

        coords = (a,b, c,d)
   
        
        masque_draw = ImageDraw.Draw(masque)
        masque_draw.rectangle(coords, fill=(0,0,0))
        diff = ImageChops.lighter(img, masque)

        diff.save("traitement_haut.jpg")
       
    def couleur_cheveux(self, image):
        self.image = image

        dico = {}

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

        print(liste2)
        for i in liste2:
            coul = couleur(i[0][0], i[0][1], i[0][2])
            
            if coul == None:
                pass
            elif coul == 'marron':
                pass
            elif coul == 'noir':
                pass
            else:
                print(coul)





    def essais(self):
        im = cv2.imread('5b.jpg')
        im[50:90,50] = 163,199,209
        cv2.imshow('image', im)
    
if __name__ == '__main__':

    
    image_femme_haut = image_femme_haut()

    #image_femme_haut.resize('9.jpg', '9.jpg')

    IMAGE = '5a.jpg'
    
    image_femme_haut.mask_bas(IMAGE)
    image_femme_haut.mask_haut(IMAGE)
    image_femme_haut.couleur_cheveux('5b.jpg')

    image_femme_haut.essais()
















































