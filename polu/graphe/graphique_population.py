import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .fonction_graphe import moyenne
from .fonction_graphe import new

def visu_population():
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT POPULATION_ACTIVE_HABITANT, nom_ville, particule FROM ville;""")
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_population(donnée):

    lyon = []
    paris = []
    marseille = []

  
    for i in donnée:
        
        if i[0] == 'None' or i[0] == None or\
           i[1] == None or i[1] == 'None'\
            or i[2] == None or i[2] == 'None':
                pass

        elif i[1] == 'lyon':
            lyon.append(int(i[2]))
        elif i[1] == 'paris':
            paris.append(int(i[2]))
        elif i[1] == 'marseille':
            marseille.append(int(i[2]))
            
        print(i)

    data = len(lyon) + len(paris) + len(marseille)
    donnée_lyon = moyenne(lyon)
    donnée_paris = moyenne(paris)
    donnée_marseille = moyenne(marseille)



    return donnée_lyon[0], donnée_paris[0], donnée_marseille[0],\
            donnée_lyon[1], donnée_paris[1], donnée_marseille[1]
   


def diagramme_population(donnée_lyon, donnée_paris, donnée_marseille,
              er_lyon, er_paris, er_marseille, save):

    plt.bar(range(3), [donnée_lyon, donnée_paris, donnée_marseille],
                        width = 0.1, color = 'red',
                       yerr = [er_lyon, er_paris, er_marseille],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['plus de 300 K', 'plus de 1M', 'plus de 500 K'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le taux de population active")

    nouveau = new()
    
    plt.savefig(nouveau)
    plt.clf()
    shutil.move(nouveau, r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')

    return nouveau
