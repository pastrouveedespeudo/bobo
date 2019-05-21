import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .fonction_graphe import *

def visu_climat(ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""SELECT météo, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste

def traitement_climat(donnée):
    beau = [0]
    nuageux = []
    pluie = []

    for i in donnée:
        if i[0] == 'beau_temps':
            beau.append(int(i[1]))

        elif i[0] == 'nuageux':
            nuageux.append(int(i[1]))

        elif i[0] == 'pluie':
            pluie.append(int(i[1]))



    donnée_beau = moyenne(beau)
    donnée_nuageux = moyenne(nuageux)
    donnée_pluie = moyenne(pluie)



    return donnée_beau[0], donnée_nuageux[0], donnée_pluie[0],\
           donnée_beau[1], donnée_nuageux[1], donnée_pluie[1]



def diagramme_climat(donnée_beau, donnée_nuageux, donnée_pluie,
              er_beau, er_nuageux, er_pluie, save):


    try:
        os.remove(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo\météo.png')
    except:
        pass
    
    plt.bar(range(3), [donnée_beau, donnée_nuageux, donnée_pluie],
                        width = 0.1, color = 'red',
                       yerr = [er_beau, er_nuageux, er_pluie],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['beau temps', 'nuageux', 'pluie'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le temps")
    
    plt.savefig(save)
    shutil.move(save, r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')










































