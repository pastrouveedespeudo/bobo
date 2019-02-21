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
    
    def point_visage(self, img):
        
        im = cv2.imread(str(img))
        img = Image.open(str(img))

        a = 40
        b = 40
        c = 40
        a  = int(round(im.shape[0] *0.25))
        b  = int(round(im.shape[0] *0.45))
        c  = int(round(im.shape[0] *0.70))

        pts1 = im[a,a]
        pts2 = im[a,b]
        pts3 = im[a,c]

        pts4 = im[b,b]
        pts5 = im[c,b]

        pts6 = im[b,a]
        pts7 = im[b,c]

        cv2.imwrite("visageonepts.jpg", im)

        return pts1, pts2, pts3, pts4, pts5, pts6 ,pts7



    def couleur_des_pts(self, pts1, pts2, pts3, pts4, pts5, pts6 ,pts7, image):
        
        print(pts1, pts2, pts3, pts4, pts5, pts6 ,pts7)
        
        PATH = r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\essais\{}".format(image)
        im = cv2.imread(str(PATH))
        
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                pass

                #balayer l'image meme princiê si la couleur +- 50 ou 100 a voir on prend
                #le reste on le met en noir
                #et on commence le mask
                #ATTENTION CROP ET MASK NE SONT PAS LA MEME CHOSE

yo = pull_tshit_short_panta()
img = yo.take_visage("one.jpg")
pts = yo.point_visage(img)

yo.couleur_des_pts(pts[0], pts[1], pts[2],pts[3],pts[4],pts[5],pts[6], "one.jpg")
















