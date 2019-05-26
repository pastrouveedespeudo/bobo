import cv2
import os


def pos_ville():

    image = 'map.png'
    path = r'C:\Users\jeanbaptiste\bobo\bobo\static\direction\{}'.format(image)

    img = cv2.imread(path)

    img[250:500,800] = 0,0,255









    
    cv2.imshow('ty', img)

pos_ville()
