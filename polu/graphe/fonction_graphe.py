import numpy as np

def moyenne(liste):
    try:
        moyenne = int(sum(liste)) / int(len(liste))
    except:
        moyenne = 0
    variance = np.var(liste)

    erreur = (variance/len(liste))**(1/2)
    return moyenne, erreur

