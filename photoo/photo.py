from PIL import ImageGrab
from PIL import *
import cv2
import os
import shutil

def photo():

    video = cv2.VideoCapture(0)

    a = 0
    
    #img = ImageGrab.grab()
    #image1 = img.save()

    while True:

        a = a + 1
        
        check, frame = video.read()

        print(check)
        print(frame)
        

        cv2.imshow("image", frame)
       

        key=cv2.waitKey(1)

        if key == ord('o'):
            break


    
    video.release()

    cv2.destroyAllWindows


    
def capture():
    
    img = ImageGrab.grab()

    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo')
    liste = os.listdir()
    for i in liste:
        print(i[0])
    new = int(i[0]) + 1
    new = str(new)
    image1 = img.save(str(new) + '.jpg')

    return new + '.jpg'



def cropage(para):

    
    img = cv2.imread(para)
    
    crop = img[320:515, 580:780]
    cv2.imwrite("gueuledemacaccropé.jpg", crop)









    
