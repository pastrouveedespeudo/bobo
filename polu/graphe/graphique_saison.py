import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np

from .fonction_graphe import moyenne

def visu_saison(ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""SELECT saison, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_saison(donnée):

    primtemps = []
    été = [0]
    hiver = [0]
    automne = [0]

    for i in donnée:
  
        if i[0] == 'primtemps':
            primtemps.append(int(i[1]))
        elif i[0] == 'été':
            été.append(int(i[1]))
        elif i[0] == 'hiver':
            hiver.append(int(i[1]))  
        elif i[0] == 'automne':
            automne.append(int(i[1])) 


    donnée_primtemps = moyenne(primtemps)
    donnée_été = moyenne(été)
    donnée_hiver = moyenne(hiver)
    donnée_automne = moyenne(automne)



    return donnée_primtemps[0], donnée_été[0], donnée_hiver[0],\
            donnée_automne[0], donnée_primtemps[1], donnée_été[1],\
            donnée_hiver[1], donnée_automne[1]


def diagramme_saison(donnée_primtemps, donnée_été, donnée_hiver, donnée_automne,
              er_primtemps, er_été, er_hiver, er_automne, save):


    plt.bar(range(4), [donnée_primtemps, donnée_été, donnée_hiver,
                       donnée_automne],
                        width = 0.1, color = 'red',
                       yerr = [er_primtemps, er_primtemps, er_été,
                              er_automne],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(4), ['primtemps', 'été', 'hiver',
                          'automne'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les saisons")
    
    plt.save(save)



















