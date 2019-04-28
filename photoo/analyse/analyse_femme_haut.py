import sys
import os
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from constante import HAAR_FACE
from constante import HAAR_YEUX

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


 
        self.im = cv2.imread('2.jpg')
        

                
        cv2.imshow('image.jpg', self.im)



        
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

    image_femme_haut.position_yeux()
    


















































