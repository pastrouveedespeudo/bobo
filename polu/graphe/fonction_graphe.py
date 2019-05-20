import numpy as np

def moyenne(liste):
    #print(liste, len(liste))
    moyenne = int(sum(liste)) / int(len(liste))

    variance = np.var(liste)

    erreur = (variance/len(liste))**(1/2)
    #print(moyenne, erreur)
    return moyenne, erreur

