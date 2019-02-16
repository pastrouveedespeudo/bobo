from PIL import ImageGrab
from PIL import *
import cv2

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


    
photo()
