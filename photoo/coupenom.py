import os
import cv2




def coupe_de_cheveux_nom(para):

    if para == "draggable14":

    
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}
 

        #faire une base de donnée pour ca

        return CHIGNON_HAUT, CHIGNON_BAS


def choix_fichier_haut(tenu):
    liste = []
    liste_vetement = []
    valeur = list(tenu.values())
    
    os.chdir(r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\vetement\{}".format(valeur[0]))
    liste = os.listdir()
    for i in liste:
        ajustage = ajustage_couleur(i, valeur[1])
        if ajustage == True:
            print(i,"ouiouaiswokiou")
            liste_vetement.append(i)

    print(liste_vetement)
    return ajustage




def ajustage_couleur(image, couleur):

    liste = []
    validation = ""
    im = cv2.imread(str(image))

    if couleur == "bleu":

        for x in range(im.shape[0]):
            for y in range(im.shape[1]):

                if im[x,y][1] <= 80 and im[x,y][1] >= 0\
                   and im[x,y][2] >= 40 and im[x,y][2] <= 120\
                   and im[x,y][0] > [x,y][1] + 40 and im[x,y][0]> im[x,y][2] + 40:
                 
                    validation = True
                

       
        if validation == True:
            print(image,"TRUREEEEEEEEEEEEEEEEE")
            liste.append(image)
        else:
            validation == False


        
   
    return validation




















