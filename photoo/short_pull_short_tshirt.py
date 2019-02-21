import cv2
from PIL import Image



class pull_tshit_short_panta:


    def take_visage(self, image):
        PATH = r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\essais\{}".format(image)

        
        img = cv2.imread(str(PATH))

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
    
            crop = img[y:h+y, x:w+x]

        cv2.imwrite("visageone.jpg", crop)
        img = "visageone.jpg"
        return img
    
    def couleur_visage(self, img):
        
        im = cv2.imread(str(img))
        img = Image.open(str(img))

        a = 40
        b = 40
        c = 40
        a  = int(round(im.shape[0] *0.25))
        b  = int(round(im.shape[0] *0.45))
        c  = int(round(im.shape[0] *0.70))

        
      
        pts1 = im[a,a] = 0,0,255#1
        pts2 = im[a,b] = 0,0,255#1
        pts3 = im[a,c] = 0,0,255#1

        pts4 = im[b,b] = 0,0,255#1
        pts5 = im[c,b] = 0,0,255#1

        pts6 = im[b,a] = 0,0,255#1
        pts7 = im[b,c] = 0,0,255#1



        cv2.imshow("lala.png", im)


        cv2.imwrite("visageonepts.jpg", im)
        cv2.imshow("lala.png", im)
        
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                pass

        
yo = pull_tshit_short_panta()
img = yo.take_visage("one.jpg")
yo.couleur_visage(img)
















