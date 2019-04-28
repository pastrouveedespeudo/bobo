import sys
import os
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import math
from constante import HAAR_FACE
from constante import HAAR_YEUX
from palettecouleur import *

##        for x in range(image.shape[0]):
##            for y in range(image.shape[1]):


class image_femme_haut:

    def resize(self):
        
       os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\photo\analyse\femme')
       image = Image.open('q.jpg')


       image = image.resize((int(round(image.width/2)),
                             int(round(image.height/2))))

       image.save('2.jpg')


       
    def ouverture(self):

        blanc = 0
        rouge = 0
        noir = 0
        bleu = 0
        vert = 0
        jaune = 0
        rose = 0

        im = cv2.imread('1.jpg')
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                coul = couleur(im[x,y][0], im[x,y][1], im[x,y][2])
                if coul == 'blanc':
                    blanc+=1
                elif coul == 'rouge':
                    rouge+=1
                elif coul == 'noir':
                    noir+=1
                elif coul == 'bleu':
                    bleu+=1
                elif coul == 'vert':
                    vert+=1
                elif coul == 'rouge':
                    rouge+=1
                elif coul == 'rose':
                    rose+=1
                elif coul == 'jaune':
                    jaune+=1
        print(blanc,
        rouge ,
        noir ,
        bleu ,
        vert ,
        jaune, 
        rose )
        cv2.imshow('image.jpg', im)



        
    def position_yeux(self):

        #nous servir pour le skin detecteur
        body_cascade = cv2.CascadeClassifier(HAAR_FACE)
        eye_cascade = cv2.CascadeClassifier(HAAR_YEUX)
        img = cv2.imread('1.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = body_cascade .detectMultiScale(gray, 1.1, 8)

        for (x,y,w,h) in faces:
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = img[y:y+h, x:x+w]
           eyes = eye_cascade.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eyes:
               cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
           
        cv2.imshow('image.jpg', img)


                        
if __name__ == '__main__':

    
    image_femme_haut = image_femme_haut()

    #image_femme_haut.resize()
    image_femme_haut.ouverture()

    #image_femme_haut.position_yeux()
    


















































