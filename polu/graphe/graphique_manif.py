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
    
    sql = ("""SELECT ACTIVITE_EXEPTIONNELLE, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_manif(donnée):
    manif = [10]
    non_manif = [0]

    for i in donnée:
        print(i)
        if i[0] == 'manifestation':
            manif.append(int(i[1]))
        elif i[0] == 'non_manifestation':
            non_manif.append(int(i[1]))

    print(non_manif)


    donnée_manif = moyenne(manif)
    donnée_non_manif = moyenne(non_manif)


    return donnée_manif[0], donnée_non_manif[0],\
            donnée_manif[1], donnée_non_manif[1]


def diagramme(donnée_manif, donnée_non_manif,
              er_manif, er_non_manif):


    
    plt.bar(range(2), [donnée_manif, donnée_non_manif],
                        width = 0.1, color = 'red',
                       yerr = [er_manif, er_non_manif],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['manifestation', 'non manifestation'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les manifestation")
    
    plt.show()





a = visu('lyon')
donnée = traitement_manif(a)

diagramme(donnée[0], donnée[1],
        donnée[2], donnée[3])






















































