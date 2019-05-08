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


    
def capture(user):
#def capture(path):
    img = ImageGrab.grab()


    liste_user = []
    direction = Accounts.objects.filter(name=user).all()
    for i in direction:
        liste_user.append(i.path_image)

    print(liste_user[0],'yoooooooooooooooojgrjporgjpogjgjpojrgejporjprge')

    try:
        os.mkdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}'.format(str(user)))
    except:
        pass
    
    os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\photo\{}'.format(str(user)))


    liste = os.listdir()
    
    liste2 = []
    
    if liste == []:
        name_picture = "1.jpg"
        img.save(str(name_picture))
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

    sauvegarde(user, str(maximum+1) + ".jpg")
    
    img.save(str(maximum + 1) + ".jpg" )

    return str(maximum + 1) + ".jpg" 



def cropage_habit(image, user):

    print(image,"55555")
    liste = []
    user = Accounts.objects.filter(name=user).all()
    for i in user:
        if image == i.photo:
            print("ouiiiiiiiiiiiiiii")
            image = i.photo
            url_image = i.photo.path
            break


    print(url_image)
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



def cropage_cheveux(image, user):

    liste = []
    user = Accounts.objects.filter(name=user).all()
    for i in user:
        if image == i.photo:
            print("ouiiiiiiiiiiiiiii")
            image = i.photo
            url_image = i.photo.path
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
    crop_img = img[250:190+300, 530:350+500]
    cv2.imwrite(str("".join(liste3[-1])), crop_img)





def sauvegarde(user, saving):

    #Accounts.objects.filter(name=user).delete()
    #Accounts.objects.create(name=user)
    
##    Accounts.objects.create(name=user, photo="yoyo.jpg")
##
##
    liste = []
    acc = Accounts.objects.filter(name=user).all()
    
    for i in acc:
        print(i.name, i.photo,'000000000')
        if i.photo == "":
            pass
        else:
            liste.append(i.photo)


    if liste == []:
        
        account = Accounts.objects.get(name=user)
        account.photo = "1.jpg"
        account.save()

    
    else:
        Accounts.objects.create(name=user, photo=saving)
        

def nom_ordi(nom, user):

    account = Accounts.objects.filter(name=user).all()
    for i in account:
        i.path_image = nom
        i.save()
        
        

    


        


        
            














































    
