import os
import cv2


def ajustage_couleur(image):#ici faudra faire genre si tu veux du vert l'ajuster

    ok = "BLEU"
    pas_ok = "PAS BLUWW"

    liste = []
    im = cv2.imread(str(image))

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):

            if im[x,y][1] <= 80 and im[x,y][1] >= 0\
               and im[x,y][2] >= 40 and im[x,y][2] <= 120\
               and im[x,y][0] > [x,y][1] + 40 and im[x,y][0]> im[x,y][2] + 40:
               
                liste.append("ok")

    if liste != [ ]:
        return ok
    else:
        return pas_ok


def coupe_de_cheveux_nom(para):

    if para == "draggable14":

        print("c'est un chignon blond")
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}
        DATE = ["2018 printemps"]

        #faire une base de donnée pour ca

        return CHIGNON_HAUT, CHIGNON_BAS


def choix_fichier_haut(tenu):
    liste = []
    valeur = list(tenu.values())
    print(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\vetement\{}".format(valeur[0]))
    os.chdir(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\vetement\{}".format(valeur[0]))
    liste = os.listdir()
    for i in liste:
        print(i)
        ajustage = ajustage_couleur(i)
        if ajustage == valeur[1]:
            liste.append(str(i))
            
    return liste























