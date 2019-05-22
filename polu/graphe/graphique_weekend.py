import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .fonction_graphe import moyenne
from .fonction_graphe import new

def visu_weekend(ville):
    print('yoooooooooooooooo')
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""SELECT WEEKEND, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_weekend(donnée):

    weekend = []
    non_weekend = []

    
    for i in donnée:
        print(i)
        if i[1] == 'None' or i[1] == None\
            or i[0] == 'None' or i[0] == None:
                pass
            
        elif i[0] == 'weekend':
            weekend.append(int(i[1]))
            
        elif i[0] == 'non_weekend':
            non_weekend.append(int(i[1]))


    data = len(weekend) + len(non_weekend)
    print(data)
    donnée_weekend = moyenne(weekend)
    donnée_non_weekend = moyenne(non_weekend)




    return donnée_weekend[0], donnée_non_weekend[0],\
            donnée_weekend[1], donnée_non_weekend[1], data
   


def diagramme_weekend(donnée_weekend, donnée_non_weekend,
              er_weekend, er_non_weekend, save):


    plt.bar(range(2), [donnée_weekend, donnée_non_weekend],
                        width = 0.1, color = 'red',
                       yerr = [er_weekend, er_non_weekend],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['weekd end', 'jour de semaine'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le weekend")
    
    nouveau = new()
    
    plt.savefig(nouveau)
    plt.clf()
    plt.close()
    shutil.move(nouveau, r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')
    return nouveau


















