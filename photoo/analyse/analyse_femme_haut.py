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
       

    def haarcascade(self, image):

        self.image = image

        cadre = []
        
        #nous servir pour le skin detecteur
        #et pour la prise de la couleur des cheveux
        
        body_cascade = cv2.CascadeClassifier(HAAR_FACE)
        eye_cascade = cv2.CascadeClassifier(HAAR_YEUX)
        img = cv2.imread(self.image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = body_cascade .detectMultiScale(gray, 1.1, 8)

        for (x,y,w,h) in faces:

           cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = img[y:y+h, x:x+w]
           cadre.append((y,h,x,w))
           eyes = eye_cascade.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eyes:
               cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                       
        #cv2.imshow('image.jpg', img)

        return cadre[0]

    def crop_visage(self, cadre, image):
        self.cadre = cadre
        self.image = image
        print(cadre)

        img = cv2.imread(self.image)
        crop_img = img[self.cadre[0]:self.cadre[0]+self.cadre[1],
                       self.cadre[2]:self.cadre[2]+self.cadre[3]]
        
        cv2.imwrite('visage.jpg', crop_img)

    def visage(self, image):
        self.image = image

        img = cv2.imread(self.image)

        x1 = img.shape[1] - 10
        y1 = img.shape[0]

        img[10,25] = 0,0,255
        img[10,40] = 0,0,255
        img[10,59] = 0,0,255




        cv2.imshow('image.jpg', img)

        




##    def peau(self, liste, im):
##        self.liste = liste
##        self.im = im
##
##        image = cv2.imread(self.im)
##        
##        for x in range(image.shape[0]):
##            for y in range(image.shape[1]):
##                for i in self.liste:
##                    if image[x,y][0] == i[0] and\
##                       image[x,y][1] == i[1] and\
##                       image[x,y][2] == i[2]:
##                        image[x,y] = 0,0,255
##                    
##        cv2.imshow('image', image)
##
##
##    def crop_chevelure(self, cadre, image):
##        self.cadre = cadre
##        self.image = image
##
##        img = cv2.imread(self.image)
##        crop_img = img[self.cadre[0][0]-10:self.cadre[0][0]+self.cadre[0][1],
##                       self.cadre[0][2]-20:self.cadre[0][2]+self.cadre[0][3]+20]
##        
##        cv2.imwrite('visage.jpg', crop_img)
##        cv2.imshow('image.jpg', crop_img)


        
if __name__ == '__main__':

    
    image_femme_haut = image_femme_haut()

    #image_femme_haut.resize('9.jpg', '9.jpg')

    IMAGE = '10.jpg'
    
    image_femme_haut.mask_bas(IMAGE)
    image_femme_haut.mask_haut(IMAGE)
    
    cadre = image_femme_haut.haarcascade(IMAGE)
    
    image_femme_haut.crop_visage(cadre, "traitement_haut.jpg")
    peau = image_femme_haut.visage("visage.jpg")

    #image_femme_haut.peau(peau, IMAGE)
















































