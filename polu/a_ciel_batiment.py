import cv2
from PIL import Image, ImageDraw, ImageChops
import numpy as np
from matplotlib import pyplot as plt

class ciel_batiment_mask:


    def ouverture_cv2(self, image):
        self.image = image

        img = cv2.imread(self.image)
        return img

    def ouverture_pil(self, image):
        self.image = image

        img = Image.open(self.image)
        return img

    def convert_gris(self, image):
        self.image = image
        img = Image.open(self.image).convert("LA")
        img.save("convert.png")

        return img


    def otsu(self):

        img = cv2.imread("polue1.jpg",0)

        ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        plt.imshow(th2,'gray')
        cv2.imwrite("otsu.png", th2)
        plt.show()

            

    def prise_du_ciel_couleur(self, image):
        self.image = image



    def delimitation_haut_bas(self, image):
        self.image = image


        
        
        a = self.image[0 :self.image.shape[0]-1,10]
        for x in range(self.image.shape[0]):
            #print(self.image[x,300], x)
            pass

        #self.image[0 :self.image.shape[0]-1,300] = 255,255,255

        
        self.image[329,300] = 255,255,255
        

        
        self.image[10,10] = 255,255,255
        self.image[100,10] = 255,255,255

        self.image[10,10] = 255,255,255
        self.image[10,100] = 255,255,255

        
        cv2.imshow("self.image", self.image)
 




        





if __name__ == "__main__":

    yo = ciel_batiment_mask()
    yo.ouverture_pil("polue2.jpg")
    
    a = yo.ouverture_cv2("polue1.jpg")
    b = yo.convert_gris("polue1.jpg")
    yo.otsu()
    
    yo.delimitation_haut_bas(a)
    








