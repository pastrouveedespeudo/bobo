import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .fonction_graphe import moyenne
from .fonction_graphe import new


def visu_pression(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    
    sql = ("""SELECT pression, nombre_particule FROM pression
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste

def traitement_pression(donnée):

    forte = [1]
    normale = []
    faible = []

    for i in donnée:
        
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'forte':
            forte.append(int(i[1]))

        elif i[0] == 'normale':
            normale.append(int(i[1]))

        elif i[0] == 'faible':
            faible.append(int(i[1]))
        print(i)

    data = len(forte) + len(normale) + len(faible)
    print(data)

    donnée_forte = moyenne(forte)
    donnée_faible = moyenne(faible)
    donnée_normale = moyenne(normale)


    return donnée_forte[0], donnée_faible[0], donnée_normale[0],\
           donnée_forte[1], donnée_faible[1], donnée_normale[1], data



def diagramme_pression(donnée_forte, donnée_faible, donnée_normale,
              er_forte, er_faible, er_normale, save):

    
    plt.bar(range(3), [donnée_forte, donnée_faible, donnée_normale],
                        width = 0.1, color = 'red',
                       yerr = [er_forte, er_faible, er_normale],
                        ecolor = 'black', capsize = 10)


    plt.xticks(range(3), ['forte pression', 'faible pression',
                          'pression normale'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon la pression en hpa")
    
    nouveau = new()
    print(nouveau)
    plt.savefig(nouveau)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau











