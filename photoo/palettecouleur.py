
#faut refaire c chiant

def couleur(couleur1, couleur2, couleur3):


    if couleur1 >= 240 and couleur1 <= 250 \
       and couleur2 >= 125 and couleur2 <= 218\
       and couleur3 >= 125 and couleur3 <= 218 and\
       couleur2 == couleur3:
        print("rose")
        
    if couleur1 <= 255 and couleur1 >= 252 \
       and couleur2 >= 145 and couleur2 <= 221\
       and couleur3 >= 145 and couleur3 <= 211\
       and couleur2 == couleur3:
        print("rose")

        

    if couleur1 <= 250 and couleur1 >= 238\
       and couleur2 <= 219 and couleur2 >= 138 \
       and couleur3 <= 216 and couleur3 >= 128:

        print('rose')


    if couleur1 <= 195 and couleur1 >= 75\
       and couleur2 <= 70 and couleur2 >= 24\
       and couleur3 <= 70 and couleur3 >= 24\
       and couleur1 >= couleur2 + 100 and couleur1 >= couleur3 + 100:
        print("rouge")



        
    if couleur1 <=  177 and couleur1 >= 75\
       and couleur2 <= 97 and couleur2 >= 37\
       and couleur3 <= 92 and couleur3 >= 35\
       and couleur3 >= couleur2 - 4:
        print("rouge")


    if couleur1 <= 180 and couleur1 >= 90\
       and couleur2 <= 70 and couleur2 >= 50\
       and couleur3 <= 87 and couleur3 >= 50\
       and couleur2 == couleur3:
        print("rouge")

    if couleur1 >= 87 and couleur1 <= 213 \
       and couleur2 >= 23 and couleur2 <= 80\
       and couleur3 >= 23 and couleur3 <= 94\
       and couleur2 == couleur3:
        print("rouge")
    

    if couleur1 <= 237 and couleur1 >= 79\
       and couleur2 >= 10 and couleur2 <= 90\
       and couleur3 <= 90 and couleur3 >= 10\
       and couleur1 >= couleur2 + 95 and couleur1 >= couleur3 + 95\
       and couleur2 <= couleur3 - 20 :
        print("rouge")

    elif couleur1 <= 255 and couleur1 >= 237\
        and couleur2 <= 65 and couleur3 <=60\
        and couleur3 <= 70\
        and couleur1 >= couleur2 + 20 and couleur1 > couleur3 + 20:
        print("rouge")

        
    if couleur1 <= 255 and couleur1 >= 241\
       and couleur2 <= 244 and couleur2 >= 205\
       and couleur3 <= 192 and couleur3 >= 138\
       and couleur3 >= couleur2 -100:
        print("jaune")

    if couleur1 <= 255 and couleur1 >= 200\
       and couleur2 <= 244 and couleur2 >= 200\
       and couleur3 <= 140 and couleur3 >= 140:
        print("jaune")


    if couleur1 <= 255 and couleur1 >= 90\
       and couleur2 <= 214 and couleur2 >= 77 \
       and couleur3 == 1 or couleur3 == 2 :
        print("jaune")

    elif couleur1 <= 255 and couleur1 >= 30\
         and couleur2 >= 60 and couleur2 <= 240\
         and couleur3 <= 170:
        print("jaune")

    if couleur1 <= 105 and couleur1 >= 0\
       and couleur2 <= 176 and couleur2 >= 80\
       and couleur3 <= 110 and couleur3 >= 170\
       and couleur2 >= couleur1 + 10:
        print("vert")


    elif couleur1 <= 204 and couleur1 >= 150\
        and couleur2 <= 238 and couleur2 >= 220\
        and couleur3 <= 255 and couleur2 >= 220:
        print("bleu")




    elif couleur1 == 1 or couleur1 == 2 or couleur1 == 3 or couleur1 ==4 \
        and couleur2 <= 88 and couleur2 >= 0\
        and couleur3 <= 244 and couleur2 >= 0\
        and couleur2 >= couleur1 - 180:
        print("bleu")


    elif couleur1 <= 204 and couleur1 >= 150\
        and couleur2 <= 238 and couleur2 >= 220\
        and couleur3 <= 255 and couleur2 >= 220:
        print("bleu")


    elif couleur1 <= 194 and couleur1 >= 0 \
         and couleur2 <= 194 and couleur2 >=0\
         and couleur3 >= 255 and couleur3 <= 255\
         and couleur1 == couleur2 and couleur2>= couleur3 + 10 :
        print("bleu")


    elif couleur1 == 0\
        and couleur2 == 0\
        and couleur3 >= 30:
        print("bleu")
        
    elif couleur1 >= 30\
        and couleur2 == 0\
        and couleur3 == 0 and\
        couleur1 >= 30:
        print("rouge")

    elif couleur1 == 0\
        and couleur2 >= 30\
        and couleur3 == 0:
        print("vert")







         
couleur(170, 180, 50)
#http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
























