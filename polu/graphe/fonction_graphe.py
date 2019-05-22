import numpy as np
import os


def moyenne(liste):
    try:
        moyenne = int(sum(liste)) / int(len(liste))
    except:
        moyenne = 0
    variance = np.var(liste)

    erreur = (variance/len(liste))**(1/2)
    return moyenne, erreur



def new():

    liste_new = []
    liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')
    for i in liste:
        
        try:
            nb = str((i[-7])) + str((i[-6])) + str((i[-5]))
            nb = int(nb)
            liste_new.append(nb)
        except:
            pass
        
        try:
            nb = str((i[-6])) + str((i[-5]))
            nb = int(nb)
            liste_new.append(nb)
        except:
            try:
                nb = int(i[-5])
                liste_new.append(nb)
            except:
                pass

    maxi = max(liste_new) + 1


        
    new_save = str(liste[-1][:-5]) + str(maxi) + '.png' 

    return new_save





















