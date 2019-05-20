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
    
    sql = ("""SELECT pression, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste

def traitement_pression(donnée):

    forte = [0]
    normale = [0]
    faible = []

    for i in donnée:
        print(i)
        if i[0] == 'forte':
            forte.append(int(i[1]))

        elif i[0] == 'normale':
            forte.append(int(i[1]))

        elif i[0] == 'faible':
            faible.append(int(i[1]))

    donnée_forte = moyenne(forte)
    donnée_faible = moyenne(faible)
    donnée_normale = moyenne(normale)


    return donnée_forte[0], donnée_faible[0], donnée_normale[0],\
           donnée_forte[1], donnée_faible[1], donnée_normale[1],



def diagramme(donnée_forte, donnée_faible, donnée_normale,
              er_forte, er_faible, er_normale):

    plt.bar(range(3), [donnée_forte, donnée_faible, donnée_normale],
                        width = 0.1, color = 'red',
                       yerr = [er_forte, er_faible, er_normale],
                        ecolor = 'black', capsize = 10)


    plt.xticks(range(3), ['forte pression', 'faible pression',
                          'pression normale'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon la pression en hpa")
    
    plt.show()



a = visu('lyon')
donnée = traitement_pression(a)

diagramme(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
          donnée[5])










