import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np

from fonction_graphe import moyenne

def visu(ville):
    
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

    weekend = [0]
    non_weekend = []


    for i in donnée:
  
        if i[0] == 'weekend':
            weekend.append(int(i[1]))
        elif i[0] == 'non_weekend':
            non_weekend.append(int(i[1]))



    donnée_weekend = moyenne(weekend)
    donnée_non_weekend = moyenne(non_weekend)




    return donnée_weekend[0], donnée_non_weekend[0],\
            donnée_weekend[1], donnée_non_weekend[1]
   


def diagramme(donnée_weekend, donnée_non_weekend,
              er_weekend, er_non_weekend):


    plt.bar(range(2), [donnée_weekend, donnée_non_weekend],
                        width = 0.1, color = 'red',
                       yerr = [er_weekend, er_non_weekend],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['weekd end', 'jour de semaine'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le weekend")
    
    plt.show()


a = visu('lyon')
donnée = traitement_weekend(a)

diagramme(donnée[0], donnée[1], donnée[2], donnée[3])
