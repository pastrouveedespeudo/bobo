import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2

from polu_ana.polution.database2 import clean_data

def visu(ville):
    
    conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')  

    cursor = conn.cursor()
    
    sql = ("""SELECT POINTE, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_heure(liste, xlabel_data):

    horraire_pointe = []
    horraire_non_pointe = []

    print(xlabel_data)
    
    for i in liste:
        #print(i[0], i[1])

        if i[0] == 'non_pointe':
            horraire_pointe.append(int(i[1]))
        
        elif i[0] == 'pointe':
            horraire_pointe.append(int(i[1]))

    if xlabel_data == 'non_pointe':
        return horraire_non_pointe

    elif xlabel_data == 'pointe':
        return horraire_pointe



def graphe_heure(ville, xlabel_data):

    clean_data()
    
    donnée = visu(ville)
    heure = traitement_heure(donnée, xlabel_data)
    
    print(heure)

    
    fig = plt.figure()

    x = [1,2,3,4,5,6]
    BarName = [7,8,9,17,18,19]

    
    height = [50,60,70,80,90,100]
    width = 0.00


    plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1.0) )
    plt.scatter([i+width/2.0 for i in x],height,color='k',s=40)

    plt.xlim(0,11)
    plt.ylim(40,150)


    plt.ylabel('Taux de pollution')
    plt.xlabel('Heure')
    plt.title('Titre')

    pylab.xticks(x, BarName, rotation=40)

    #plt.savefig('HeurePointeBeauSemaine.png')
    #plt.show()




graphe_heure('lyon', 'pointe')
print('\n')
graphe_heure('lyon', 'non_pointe')


