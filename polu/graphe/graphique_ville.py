import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .fonction_graphe import moyenne

def visu():
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT nom_ville, particule FROM ville;""")
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_ville(donnée):

    lyon = []
    paris = []
    marseille = []

    for i in donnée:
  
        if i[0] == 'lyon':
            lyon.append(int(i[1]))
        elif i[0] == 'paris':
            paris.append(int(i[1]))
        elif i[0] == 'marseille':
            marseille.append(int(i[1]))


    donnée_lyon = moyenne(lyon)
    donnée_paris = moyenne(paris)
    donnée_marseille = moyenne(marseille)



    return donnée_lyon[0], donnée_paris[0], donnée_marseille[0],\
            donnée_lyon[1], donnée_paris[1], donnée_marseille[1]
   


def diagramme(donnée_lyon, donnée_paris, donnée_marseille,
              er_lyon, er_paris, er_marseille):

    try:
        os.remove(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo\diagramme.png')
    except:
        pass
    plt.bar(range(3), [donnée_lyon, donnée_paris, donnée_marseille],
                        width = 0.1, color = 'red',
                       yerr = [er_lyon, er_paris, er_marseille],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['lyon', 'paris', 'marseille'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les villes")
    
    plt.show()
    shutil.move(save, r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')


