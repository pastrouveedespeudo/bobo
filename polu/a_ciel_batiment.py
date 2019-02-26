import os
import re
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageChops
from statistics import mean


class expé:


    def roi(self):
        
        im = cv2.imread("lyon 92.jpg")
        #cv2.imshow("self.image1", im)
        x = 320
        y = 210
        h = 40
        w = 50
        #320 210 40 50 
        x1 = 340
        y1 = 355
        h1 = 55
        w1 = 55
        #340 355 55 55
        x2 = 290
        y2 = 500
        h2 = 50
        w2 = 80
        #290 500 50 80        
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,0,255),2)
        crop = im[y:y+h, x:x+w]
        cv2.rectangle(im, (x1,y1),(x1+w1,y1+h1),(0,255,0),2)
        crop2 = im[y1:y1+h1, x1:x1+w1]
        cv2.rectangle(im, (x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        crop3 = im[y2:y2+h2, x2:x2+w2]

        cv2.imshow("self.image", im)
        #cv2.imshow("self.image2", crop)
        cv2.imwrite("contour1.png", crop)
        cv2.imwrite("contour2.png", crop2)
        cv2.imwrite("contour3.png",crop3)







    def image_gris(self):
       
        im = cv2.imread("1_1000_3000m3.jpg")
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("yo.png", imgray)
        cv2.imwrite("coucou.png", imgray)

        im = cv2.imread("coucou.png")
     

        x = 140
        y = 60
        h = 40
        w = 50
        
        x1 = 55
        y1 = 10
        h1 = 62
        w1 = 55

        x2 = 1
        y2 = 1
        h2 = 50
        w2 = 50
        
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,0,255),2)
        crop = im[y:y+h, x:x+w]
        cv2.rectangle(im, (x1,y1),(x1+w1,y1+h1),(0,255,0),2)
        crop2 = im[y1:y1+h1, x1:x1+w1]
        cv2.rectangle(im, (x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        crop3 = im[y2:y2+h2, x2:x2+w2]

        cv2.imshow("self.image", crop)
        cv2.imshow("self.image2", crop2)
        cv2.imshow("self.image3", crop3)
        
        cv2.imwrite("contour1_nb.png", crop)
        cv2.imwrite("contour2_nb.png", crop2)
        cv2.imwrite("contour3_nb.png",crop3)

 
    def contraste(self):
        #luminance0.2126*R+0.7152*V+0.0722*B
        #faire la moyenne
        #contraste = limage - lfond/lfond

        #bvr
        liste_image = []
        liste_fond = []
        liste_image_pres = []
        liste_image_loin = []

        
        lumi_fond = cv2.imread("lyon 92.jpg")
        for x in range(lumi_fond.shape[0]):
            for y in range(lumi_fond.shape[1]):
                a = lumi_fond[x,y][2] * 0.2126
                b = lumi_fond[x,y][1] * 0.7152
                c = lumi_fond[x,y][0] * 0.0722
                total = a + b + c
                liste_image.append(total)
                #print(total)


        lumi_fond = cv2.imread("contour1.png")
        for x in range(lumi_fond.shape[0]):
            for y in range(lumi_fond.shape[1]):
                a = lumi_fond[x,y][2] * 0.2126
                b = lumi_fond[x,y][1] * 0.7152
                c = lumi_fond[x,y][0] * 0.0722
                total = a + b + c
                liste_fond.append(total)
                #print(total)

                
        lumi_im_pres = cv2.imread("contour2.png")
        for x in range(lumi_im_pres.shape[0]):
            for y in range(lumi_im_pres.shape[1]):
                a = lumi_im_pres[x,y][2] * 0.2126
                b = lumi_im_pres[x,y][1] * 0.7152
                c = lumi_im_pres[x,y][0] * 0.0722
                total = a + b + c
                liste_image_pres.append(total)
                #print(total)


        lumi_im_loin = cv2.imread("contour3.png")
        for x in range(lumi_im_loin.shape[0]):
            for y in range(lumi_im_loin.shape[1]):
                a = lumi_im_loin[x,y][2] * 0.2126
                b = lumi_im_loin[x,y][1] * 0.7152
                c = lumi_im_loin[x,y][0] * 0.0722
                total = a + b + c
                liste_image_loin.append(total)
                #print(total)


   
        print(a = mean(liste_fond))
        print(b = mean(liste_image))
        print(c = mean(liste_image_pres))
        print(d = mean(liste_image_loin))
        
        #bon au pire ca revient au meme
    
        constrasteLocalb = (a - b)/a
        constrasteLocalc = (a - c)/a
        constrasteLocald = (a - d)/a

        print(constrasteLocalb)
        print(constrasteLocalc)
        print(constrasteLocald)
        

        
        

        #contrastelocal = (limage - lcontour3)/limage

        #cherche une coreelation entre deux contraste
        #si constrabe b - constrate a = x
        #alors x == tant de pm
        #et ensuite qualibre ca sur plusieur jour selon les images
        #et fais un tout
        
        #. Par conséquent, plus la concentration en PM est élevée,
        #plus le contraste de l'image est faible.
        
        
yo = expé()
yo.roi()
#yo.image_gris()
#yo.contraste()
