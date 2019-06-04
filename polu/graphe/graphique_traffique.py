import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .fonction_graphe import moyenne
from .fonction_graphe import new


def visu_traffique(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""SELECT TRAFIQUE, nombre_particule FROM traffique
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_traffique(donnée):
    depart_routier = []
    regulier_jour = []

 
    for i in donnée:
    
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'regulier jour':
            regulier_jour.append(int(i[1]))
        elif i[0] == 'depart_routier':
            depart_routier.append(int(i[1]))

        print(i)
        
    data = len(depart_routier) + len(regulier_jour)
    print(data)

    donnée_regulier_jour = moyenne(regulier_jour)
    donnée_depart_routier = moyenne(depart_routier)

    return donnée_regulier_jour[0], donnée_depart_routier[0],\
            donnée_regulier_jour[1], donnée_depart_routier[1], data

def diagramme_traffique(donnée_regulier_jour, donnée_depart_routier,
              er_regulier_jour, er_depart_routier, save):


    
    plt.bar(range(2), [donnée_regulier_jour, donnée_depart_routier],
                        width = 0.1, color = 'red',
                       yerr = [er_regulier_jour, er_depart_routier],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['régulier jour', 'départ routier'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les départ routiers")

    nouveau = new()
    
    plt.savefig(nouveau)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau
























































