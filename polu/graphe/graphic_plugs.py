import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .fonction_graphe import moyenne
from .fonction_graphe import new



def visu_plugs(city):
    """We ask database about plugs"""
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    cursor = conn.cursor()
    
    sql = ("""SELECT BOUCHON, nombre_particule FROM bouchon
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_plugs(donnée):
    """We tidy conditions into list and make an average"""

    
    liste = ['non', 'petit', 'moyen', 'grand', 'assez grand',
             'tres grand']
    non = []
    petit = []
    moyen = []
    grand = []
    assez_grand = []
    tres_grand = []
    

    for i in donnée:
        print(i[0])


        
        if i[1] == 'None' or i[1] == None\
            or i[0] == 'None' or i[0] == None:
                pass
        elif i[0] == 'non':
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
            

    data = len(non) + len(petit) + len(moyen) + len(grand)+ len(assez_grand)+ len(tres_grand)
    print(data)
    
    donnée_non = moyenne(non)

    donnée_petit = moyenne(petit)

    donnée_moyen = moyenne(moyen)

    donnée_grand = moyenne(grand)

    donnée_assez_grand = moyenne(assez_grand)

    donnée_tres_grand = moyenne(tres_grand) #We make an average by function_graph

    return donnée_non[0], donnée_petit[0], donnée_moyen[0],\
            donnée_grand[0], donnée_assez_grand[0],\
            donnée_tres_grand[0],\
            donnée_non[1], donnée_petit[1], donnée_moyen[1],\
            donnée_grand[1], donnée_assez_grand[1],\
            donnée_tres_grand[1], data




def diagram_plugs(donnée_non, donnée_petit, donnée_moyen,
              donnée_grand, donnée_assez_grand,
              donnée_tres_grand,
              er_non, er_petit, er_moyen,
              er_grand, er_assez_grand,
              er_tres_grand, save):

    """We siplay it into a matplotlab graph"""
    
    
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


    nouveau = new()
    print(nouveau)
    plt.savefig(nouveau)
    plt.clf()               #we empty the cache
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')    #Move graph to popo file
    return nouveau





































