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
    
    sql = ("""SELECT TRAFIQUE, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_traffique(donnée):
    depart_routier = [0]
    regulier_jour = []

    
    for i in donnée:

        if i[0] == 'regulier jour':
            regulier_jour.append(int(i[1]))
        elif i[0] == 'depart_routier jour':
            depart_routier.append(int(i[1]))


    donnée_regulier_jour = moyenne(regulier_jour)
    donnée_depart_routier = moyenne(depart_routier)

    return donnée_regulier_jour[0], donnée_depart_routier[0],\
            donnée_regulier_jour[1], donnée_depart_routier[1]

def diagramme(donnée_regulier_jour, donnée_depart_routier,
              er_regulier_jour, er_depart_routier):


    plt.bar(range(2), [donnée_regulier_jour, donnée_depart_routier],
                        width = 0.1, color = 'red',
                       yerr = [er_regulier_jour, er_depart_routier],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['départ routier', 'régulier jour'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les départ routiers")
    
    plt.show()










a = visu('lyon')
donnée = traitement_traffique(a)

diagramme(donnée[0], donnée[1], donnée[2], donnée[3])















































