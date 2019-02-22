
#faut refaire c chiant

def couleur(couleur1, couleur2, couleur3):
    if couleur1 >= 216 and couleur1<=255\
       and couleur2 >= 105 and couleur2 <= 191\
       and couleur3 <= 216 and couleur3 >= 150:
        print("violet, rose")

    if couleur1 >= 30 and couleur1 <= 255\
       and couleur3 >= 30 and couleur3 <= 255\
       and couleur2 <= couleur1 - 100 and couleur3 - 100:
        print("rose")

    elif couleur1 <= 255 and >= 30\
        and couleur2 <= 110 and couleur3 <= 70\
        and couleur1 >= couleur2 + 20 and couleur1 > couleur3 + 20:
        print("rouge")
        

    elif couleur1 <= 255 and couleur1 >= 30\
         and couleur2 >= 60 and <= 240\
         and couleur3 <= 170:
        print("jaune")
        
    elif couleur1 <= 255 and couleur1 >= 30\
         and couleur2 >= 30 and couleur2 <= 255\
         and couleur3 >= 0 and couleur3 <= 180\
         and couleur2 >= couleur1 + 20 and couleur2 >= couleur1 + 20:
        print("vert")

    elif couleur1 <= 210 and couleur1 >= 0 \
         and couleur2 <= 200 and couleur2 >=0\
         and couleur3 >=30 and couleur3 <= 255\
         and couleur3 >= couleur2 + 20 and couleur3 > couleur1 + 20:
        print("bleu")
         
couleur(248, 159, 179)
#http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
