import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .fonction_graphe import moyenne


def visu_bouchon(ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""SELECT BOUCHON, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste

def traitement_bouchon(donnée):
    liste = ['non', 'petit', 'moyen', 'grand', 'assez grand',
             'tres grand']
    non = [0]
    petit = [0]
    moyen = [0]
    grand = [0]
    assez_grand = [0]
    tres_grand = [0]
    
    try:
        for i in donnée:
            if i[0] == 'non':
                non.append(int(i[1]))
            elif i[0] == 'petit':
                petit.append(int(i[1]))
            elif i[0] == 'moyen':
                moyen.append(int(i[1]))  
            elif i[0] == 'grand':
                grand.append(int(i[1]))
            elif i[0] == 'assez grand':
                assez_grand.append(int(i[1]))
            elif i[0] == 'tres grand':
                tres_grand.append(int(i[1]))
    except:
        pass
    #print(non, petit, moyen, grand, assez_grand, tres_grand)


    donnée_non = moyenne(non)

    donnée_petit = moyenne(petit)

    donnée_moyen = moyenne(moyen)

    donnée_grand = moyenne(grand)

    donnée_assez_grand = moyenne(assez_grand)

    donnée_tres_grand = moyenne(tres_grand)

    return donnée_non[0], donnée_petit[0], donnée_moyen[0],\
            donnée_grand[0], donnée_assez_grand[0],\
            donnée_tres_grand[0],\
            donnée_non[1], donnée_petit[1], donnée_moyen[1],\
            donnée_grand[1], donnée_assez_grand[1],\
            donnée_tres_grand[1]




def diagramme_bouchon(donnée_non, donnée_petit, donnée_moyen,
              donnée_grand, donnée_assez_grand,
              donnée_tres_grand,
              er_non, er_petit, er_moyen,
              er_grand, er_assez_grand,
              er_tres_grand, save):
    try:
        os.remove(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo\diagramme_bouchon.png')
    except:
        pass
    
    plt.bar(range(6), [donnée_non, donnée_petit, donnée_moyen,
                       donnée_grand, donnée_assez_grand,
                        donnée_tres_grand],
                        width = 0.1, color = 'red',
                       yerr = [er_non, er_petit, er_moyen,
                              er_grand, er_assez_grand,
                              er_tres_grand],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(6), ['non', 'petit', 'moyen',
                          'grand', 'assez grand', 'tres grand'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les bouchons")
    
    plt.savefig(save)
    shutil.move(save, r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')







































