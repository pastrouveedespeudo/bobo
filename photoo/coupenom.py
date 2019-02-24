import os
import cv2
from colour import Color









def coupe_de_cheveux_nom(para):

    if para == "draggable" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "rouge"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable1" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "rouge"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"rouge"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable2" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "noir"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable3" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "blanc"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable4" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "rouge"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"rouge"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable5" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable6" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"rouge"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable7" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "orange"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"vert"}

        return CHIGNON_HAUT, CHIGNON_BAS
    
    elif para == "draggable8" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "gris"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable9" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable10" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"marron"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable11" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "vert"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS
    
    elif para == "draggable12" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"blanc"}

        return CHIGNON_HAUT, CHIGNON_BAS
    
    elif para == "draggable13" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "noir"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable14":
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    elif para == "draggable15" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "vert"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable16" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "orange"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable17" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "gris"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable18" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "bleu"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"noir"}

        return CHIGNON_HAUT, CHIGNON_BAS

    
    elif para == "draggable19" :
        CHIGNON_HAUT = {"haut":"t-shirt ", "hautcouleur": "rouge"}
        CHIGNON_BAS = {"bas":"jean", "couleurbas":"bleu"}

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
                
    if couleur == "rouge":

        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                
                if im[x,y][0] <= 80 and im[x,y][0] >= 0\
                   and im[x,y][1] >= 40 and im[x,y][1] <= 120\
                   and im[x,y][2] > [x,y][1] + 40 and im[x,y][2]> im[x,y][0] + 40:

                    validation = True
                    break
                
        if validation == True:

            liste.append(image)
        else:
            validation == False

            
    return validation



def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

print(rgb_to_hex((255, 255, 255))  )
print(Color("#ff0000"))
#fais tout crash

















