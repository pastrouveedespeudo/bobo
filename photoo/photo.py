from PIL import ImageGrab
from PIL import *
import cv2
import os
import shutil

from accounts.models import Accounts

from .models import *

from .coupe_dico import DICO_COIF2
from .coupe_dico import DICO_COIF3

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


    
def capture(user, format_image):

    img = ImageGrab.grab()



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
            img.save(str(name_picture))

     
            acc = Accounts.objects.filter(name=user).all()
            for i in acc:
                i.photo_cheveux = name_picture
                i.save()
                
            return name_picture

        elif format_image == "habit":
            name_picture = "1.jpg"
            img.save(str(name_picture))
            
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
    
    img.save(str(maximum + 1) + ".jpg" )

    return str(maximum + 1) + ".jpg" 



def cropage_habit(image, user, format):

    print(image,"55555")
    
    liste = []
      
    if format == 'habit':
        print("ouiiiiiiiiiiiiiiiiiiiiii")
        user = Accounts.objects.filter(name=user).all()
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

    img = cv2.imread("".join(liste3[-1]))
    crop_img = img[300:170+300, 530:350+500]
    cv2.imwrite(str("".join(liste3[-1])), crop_img)



def cropage_cheveux(image, user, format):

    print(image)
    
    liste = []

    if format == 'cheveux':
        user = Accounts.objects.filter(name=user).all()
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

    
        img = cv2.imread("".join(liste3[-1]))
        crop_img = img[250:190+300, 530:350+500]
        cv2.imwrite(str("".join(liste3[-1])), crop_img)


    except:
        pass


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
    
    


def affichage_coupe_fav(username):
    
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
        
            














































    
