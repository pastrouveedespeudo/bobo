import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .function_graph import moyenne
from .function_graph import new

def visu():
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    cursor = conn.cursor()
    
    cursor.execute("""SELECT nom_ville, nombre_particule FROM condition2;""")
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_ville(donnée):

    lyon = []
    paris = []
    marseille = []

    for i in donnée:
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'lyon':
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


    plt.bar(range(3), [donnée_lyon, donnée_paris, donnée_marseille],
                        width = 0.1, color = 'black',
                       yerr = [er_lyon, er_paris, er_marseille],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['lyon', 'paris', 'marseille'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les villes")
    
    nouveau = new()
        
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    shutil.move(save, '/app/static/popo')

    return nouveau
















