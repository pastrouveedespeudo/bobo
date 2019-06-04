import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .fonction_graphe import moyenne
from .fonction_graphe import new

def visu_manif(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""SELECT ACTIVITE_EXEPTIONNELLE, nombre_particule FROM activité
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_manif(donnée):
    manif = []
    non_manif = []
    
    for i in donnée:
        print(i)
        if i[1] == 'None' or i[1] == None\
           or i[0] == 'None' or i[0] == None:
            pass
        elif i[0] == 'manifestation':
            manif.append(int(i[1]))
        elif i[0] == 'non_manifestation':
            non_manif.append(int(i[1]))



    data = len(manif) + len(non_manif)
    print(data)


    donnée_manif = moyenne(manif)
    donnée_non_manif = moyenne(non_manif)


    return donnée_manif[0], donnée_non_manif[0],\
            donnée_manif[1], donnée_non_manif[1], data


def diagramme_manif(donnée_manif, donnée_non_manif,
              er_manif, er_non_manif, save):


    
    plt.bar(range(2), [donnée_manif, donnée_non_manif],
                        width = 0.1, color = 'red',
                       yerr = [er_manif, er_non_manif],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['manifestation', 'non manifestation'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les manifestation")
    
    nouveau = new()
    
    plt.savefig(nouveau)
    plt.clf()
    shutil.move(nouveau, '/app/static/popo')
    return nouveau


























































