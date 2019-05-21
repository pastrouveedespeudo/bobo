import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np

from .fonction_graphe import moyenne

def visu_vent(ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""SELECT vent, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_vent(donnée):

    tres_fort = [0]
    fort = []
    moyen = []
    faible = []
 
    for i in donnée:
        print(i)
        if i[0] == 'tres fort':
            tres_fort.append(int(i[1]))
        
        elif i[0] == 'fort':
            fort.append(int(i[1]))

        elif i[0] == 'moyen fort':
            moyen.append(int(i[1]))

        elif i[0] == 'faible':
            faible.append(int(i[1]))

    donnée_tres_fort = moyenne(tres_fort)
    donnée_fort = moyenne(fort)
    donnée_moyen = moyenne(moyen)
    donnée_faible = moyenne(faible)

    
    return donnée_tres_fort[0], donnée_fort[0],\
           donnée_moyen[0], donnée_faible[0],\
           donnée_tres_fort[1], donnée_fort[1],\
           donnée_moyen[1], donnée_faible[1]


def diagramme_vent(donnée_tres_fort, donnée_fort,donnée_moyen, donnée_faible,
              er_donnée_tres_fort, er_fort, er_moyen, er_faible, save):


    plt.bar(range(4), [donnée_tres_fort, donnée_fort,
                       donnée_moyen, donnée_faible],
                        width = 0.1, color = 'red',
                       yerr = [er_donnée_tres_fort, er_fort,
                               er_moyen,er_faible],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(4), ['vent tres fort', 'vent fort', 'vent moyen','vent faible'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le vent en km/h")
    
    plt.save(save)




























