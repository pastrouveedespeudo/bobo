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

    liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')

    try:
        nb = str((liste[-1][-3])) + str((liste[-1][-4])) + str((liste[-1][-5]))
        nb = int(nb) + 1
    except:
        pass
    
    try:
        nb = str((liste[-1][-4])) + str((liste[-1][-5]))
        nb = int(nb) + 1
    except:
        nb = int(liste[-1][-5]) + 1
        
    new_save = str(liste[-1][:-5]) + str(nb) + '.png' 

    return new_save
