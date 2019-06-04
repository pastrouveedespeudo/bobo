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
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    cursor.execute("""SELECT POPULATION_ACTIVE_HABITANT,
                    nom_ville,
                    nombre_particule FROM conditions2;""")
    
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
    shutil.move(nouveau, '/app/static/popo')

    return nouveau
