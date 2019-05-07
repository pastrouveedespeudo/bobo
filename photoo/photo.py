from PIL import ImageGrab
from PIL import *
import cv2
import os
import shutil

from accounts.models import Accounts

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



def cropage():

    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo')
    liste = os.listdir()
    for i in liste:
        print(i[0])
        
    img = cv2.imread(i)
    
    crop = img[320:515, 580:780]

    new = int(i[0]) + 1
    new = str(new)
    
    cv2.imwrite(str(new) + '.jpg', crop)


    return new + '.jpg'


#soit prend la couleur du front


def photo_database(user):
    
    acc = Accounts.objects.get(name=user)
    print(acc.name,"000000000000000000000000000000000000000000000000")
    
    print(acc.photo)
    if acc.photo == "":
        acc.photo = "1.jpg"
        acc.save()

    else:
        print(acc.photo)
















































    
