import cv2
import os


def pos_ville():

    image = 'map.jpg'
    path = r'C:\Users\jeanbaptiste\bobo\bobo\direction\carte\{}'.format(image)

    image = cv2.imread(path)

    direction = 0
    x = 10
    y = 50
    image[50,84] = 0,0,255
    #1052 37,
    #580 20

    cv2.imshow('ty', image)










pos_ville()























































##if direction == 0 or direction == 360 or direction > 337.5:
##        cv2.line(image, (x, y), (x, y-30), (0, 0, 255))#0-360
##
##    elif direction > 0 and direction <= 22.5:
##        cv2.line(image, (x, y), (x + 10, y - 25), (0, 0, 255))#22.5
##
##    elif direction > 22.5 and direction <= 45:
##        cv2.line(image, (x, y), (x + 20, y - 20), (0, 0, 255))#45
##
##    elif direction > 45 and direction <= 67.5:
##        cv2.line(image, (x, y), (x + 30, y - 15), (0, 0, 255))#67.5
##
##    elif direction > 67.5 and direction <= 90:
##        cv2.line(image, (x, y), (x + 30, y), (0, 0, 255))#90
##
##    elif direction > 90 and direction <= 112.5:
##        cv2.line(image, (x, y), (x + 30, y + 15), (0, 0, 255))#112.5
##
##    elif direction > 112.5 and direction <= 135:
##        cv2.line(image, (x, y), (x + 22, y + 22), (0, 0, 255))#135
##
##    elif direction > 135 and direction <= 157.5:
##        cv2.line(image, (x, y), (x + 10, y + 30), (0, 0, 255))#157.5
##
##    elif direction > 157.5 and direction <= 180:
##        cv2.line(image, (x, y), (x, y+30), (0, 0, 255))#180
##        
##    elif direction > 180 and direction <= 202.5:
##        cv2.line(image, (x, y), (x - 10, y + 30), (0, 0, 255))#202.5
##
##    elif direction > 202.5 and direction <= 225:
##        cv2.line(image, (x, y), (x - 23, y + 23), (0, 0, 255))#225
##
##    elif direction > 225 and direction <= 247.5:
##        cv2.line(image, (x, y), (x - 28, y + 13), (0, 0, 255))#247.5
##
##    elif direction > 247.5 and direction <= 270:
##        cv2.line(image, (x, y), (x - 30, y), (0, 0, 255))#270
##
##    elif direction > 270 and direction <= 292.5:
##        cv2.line(image, (x, y), (x - 10, y - 25), (0, 0, 255))#292.5
##        
##    elif direction > 292.5 and direction <= 315:
##        cv2.line(image, (x, y), (x - 20, y - 20), (0, 0, 255))#315
##        
##    elif direction > 315 and direction <= 337.5:
##        cv2.line(image, (x, y), (x - 30, y - 13), (0, 0, 255))#337.5













