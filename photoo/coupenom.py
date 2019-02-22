import os
import cv2


#la normalmeent tu fois faire une fonction qui apel la base de donnée
#tu dois faire un truk qui rajoute aussi
#bon au pire nik
def coupe_de_cheveux_nom(para):

    if para == "draggable" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable1" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable2" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable3" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable4" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable5" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable6" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable7" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS
    
    elif para == "draggable8" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable9" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable10" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable11" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS
    
    elif para == "draggable12" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS
    
    elif para == "draggable13" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable14":
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    elif para == "draggable15" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable16" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable17" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable18" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable19" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    

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
            liste_vetement.append(i)

    print(liste_vetement)
    return liste_vetement




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

            liste.append(image)
        else:
            validation == False


        
   
    return validation




















