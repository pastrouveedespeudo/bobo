from PIL import *
from PIL import Image


import cv2
import numpy as np

import os
import shutil

from accounts.models import Accounts

from .models import *

from .coupe_dico import DICO_COIF2
from .coupe_dico import DICO_COIF3



def photographie():

    
    video = cv2.VideoCapture(0)
    a = 0
    while True:

        a = a + 1
        
        check, frame = video.read()

        print(check)
        print(frame)
        

        cv2.imshow("image", frame)
       

        key=cv2.waitKey(1)

        if key == ord('o'):
            cv2.imwrite('yoyoyo.jpg', frame)
            break



    video.release()



##    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
##    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    ret, frame = cap.read()
        
    cv2.imwrite('image.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

    
def capture(user, format_image):

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    

            
    try:
        os.mkdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}'.format(str(user)))
        
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}'.format(str(user)))
        os.mkdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\habit'.format(str(user)))

        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}'.format(str(user)))
        os.mkdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\cheveux'.format(str(user)))
        
    except:
        pass

    if format_image == "cheveux":
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\cheveux'.format(str(user)))
    elif format_image == "habit":
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\habit'.format(str(user)))



    liste = os.listdir()
    
    liste2 = []
    
    if liste == []:
        
        if format_image == "cheveux":
            name_picture = "1.jpg"
            cv2.imwrite(str(name_picture), frame)
            cap.release()
            #img.save(str(name_picture))

     
            acc = Accounts.objects.filter(name=user).all()
            for i in acc:
                i.photo_cheveux = name_picture
                i.save()
                
            return name_picture

        elif format_image == "habit":
            name_picture = "1.jpg"
            #img.save(str(name_picture))
            cv2.imwrite(str(name_picture), frame)
            cap.release()
            
            acc = Accounts.objects.filter(name=user).all()
            for i in acc:
                i.photo_habit = name_picture
                i.save()
                
            return name_picture
        
    else:
        for i in liste:
            try:
                try:
                    save = i[:2]
                    save = int(save)
                    if save == int(save): 
                        liste2.append(int(save))
                    
                except:
                    liste2.append(int(i[0]))
            except:
                pass
            
    print(liste2)
    maximum = max(liste2)

    sauvegarde(user, str(maximum+1) + ".jpg", format_image)
    
    cv2.imwrite(str(maximum + 1) + ".jpg", frame)
    cap.release()
    return str(maximum + 1) + ".jpg" 



def haar(image, user, format):

    try:
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\photo')
        liste = os.listdir()
        print(liste)
        
        fichier = r'C:\Users\jeanbaptiste\bobo\bobo\photo\haarcascade_frontalface_default.xml'
        fichier_copy = r'C:\Users\jeanbaptiste\bobo\bobo\photo\haarcascade_frontalface_default_copy.xml'
        
        shutil.copy(fichier, fichier_copy)


        path = r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}\{}'
        path_user = path.format(user, format)
        print(path_user, '0000000000000000000000000000000000000000000000000000000000000000000000000000')

        shutil.move(fichier_copy, path_user)
      
    except:
        pass

    try:
        os.chdir(path_user)
        
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default_copy.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x-1000,y-1000),(x-1000+w+100,y-1000+h+1000),0)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            crop = img[y-20:h+20+y, x-20:w+20+x]

        cv2.imwrite(image, crop)
        
    except:
        return 'error'

def noir_blanc(image):
    
    im = cv2.imread(image, 0)
    cv2.imwrite(image, im)

def resize(image):
    im = Image.open(image)
    im = im.resize((100,100))
    im.save(image)




def cropage_habit(image, the_user, format):

    print(image,"55555")
    print(the_user)
    
    liste = []
      
    if format == 'habit':
        print("ouiiiiiiiiiiiiiiiiiiiiii")
        user = Accounts.objects.filter(name=the_user).all()
        for i in user:
            print(i.photo_habit,'55555555555555555555555555555555')
            if image == i.photo_habit:
                print("ouiiiiiiiiiiiiiii")
                image = i.photo_habit
                url_image = i.photo_habit.path
                break
            
 
    liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[]]
    
    c = 0
    for i in url_image:
        if i == "\\":
            c+=1
        else:
            liste2[c].append(i)
            
    print(liste2)
    liste3 = []
    for i in liste2:
        if i == []:
            pass
        else:
            liste3.append(i)

    print(liste3)
    print("".join(liste3[-1]),'000000000000000000000000000000000')

    
    img = cv2.imread("".join(liste3[-1]))
    
    cv2.imwrite(str("".join(liste3[-1])), img)
   
    error = haar("".join(liste3[-1]), the_user, 'habit')
    if error == 'error':
        return 'error'
    else:
        noir_blanc("".join(liste3[-1]))
        resize("".join(liste3[-1]))
  
        

def cropage_cheveux(image, the_user, format):

    print(image)
    
    liste = []

    if format == 'cheveux':
        user = Accounts.objects.filter(name=the_user).all()
        for i in user:
            if image == i.photo_cheveux:
                print("ouiiiiiiiiiiiiiii")
                image = i.photo_cheveux
                url_image = i.photo_cheveux.path
                break

            
    liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[]]

    try:
        c = 0
        for i in url_image:
            if i == "\\":
                c+=1
            else:
                liste2[c].append(i)
                
        print(liste2)
        liste3 = []
        for i in liste2:
            if i == []:
                pass
            else:
                liste3.append(i)

        print(liste3)
        
    except:
        pass
    
    
    img = cv2.imread("".join(liste3[-1]))
    #crop_img = img[250:190+300, 530:350+500]
    cv2.imwrite(str("".join(liste3[-1])), img)
    error = haar("".join(liste3[-1]), the_user, 'cheveux')
    if error == 'error':
        return 'error'
    else:
        noir_blanc("".join(liste3[-1]))
        resize("".join(liste3[-1]))



def sauvegarde(user, saving, format):

    #Accounts.objects.filter(name=user).delete()
    #Accounts.objects.create(name=user)
    
##    Accounts.objects.create(name=user, photo="yoyo.jpg")
##
##
    liste = []
    acc = Accounts.objects.filter(name=user).all()

    if format == 'cheveux':
        for i in acc:
            print(i.name, i.photo_cheveux,'000000000')
            if i.photo_cheveux == "":
                pass
            else:
                liste.append(i.photo_cheveux)
                
    elif format == 'habit':
        for i in acc:
            print(i.name, i.photo_habit,'000000000')
            if i.photo_habit == "":
                pass
            else:
                liste.append(i.photo_habit)

                
    if liste == []:
        
        if format == "habit":
            account = Accounts.objects.get(name=user)
            account.photo_habit = "1.jpg"
            account.save()
            
        elif format == "cheveux":
            account = Accounts.objects.get(name=user)
            account.photo_cheveux = "1.jpg"
            account.save()
    
    else:
        if format == "habit":
            Accounts.objects.create(name=user, photo_habit=saving)
        elif format == "cheveux":
            Accounts.objects.create(name=user, photo_cheveux=saving)
        



def nom_ordi(nom, user):

    account = Accounts.objects.filter(name=user).all()
    for i in account:
        i.path_image = nom
        i.save()
        
        
def coupe_fav(user_current, coupe, largeur_im, hauteur_im):


    largeur_im = int(largeur_im)
    hauteur_im = int(hauteur_im)

    favoris.objects.create(user=user_current, coiffure=coupe,
                           hauteur=int(hauteur_im),
                           largeur=int(largeur_im))
    
    


def displaying_favorite_haircut(username):
    
    acc = favoris.objects.filter(user=username).all()

    liste_coif = []

    
    liste1 = []
    liste_larg = []
    liste_haut = []

    
    for i in acc:
        liste1 = []
        for cle, valeur in DICO_COIF2.items():
            if i.coiffure == cle:
                liste1.append(DICO_COIF2[cle])
               
                
        
        for cle, valeur in DICO_COIF2.items():
            if i.coiffure == cle:
                liste1.append(DICO_COIF3[cle])
                
                

                
        liste1.append(i.largeur)
        liste1.append(i.hauteur)

        liste_coif.append(liste1)

    print(liste_coif)
    return liste_coif
        
            














































    
