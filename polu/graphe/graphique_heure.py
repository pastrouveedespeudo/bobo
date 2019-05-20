import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np

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


def traitement_heure(ville):

    horraire_pointe = []
    horraire_non_pointe = []

    donnée = visu(ville)


    for i in donnée:
        #print(i[0], i[1])

        if i[0] == 'non_pointe':
            horraire_non_pointe.append(int(i[1]))
        
        elif i[0] == 'pointe':
            horraire_pointe.append(int(i[1]))

    
    moy = sum(horraire_pointe) / len(horraire_pointe)
    variance_pointe = np.var(horraire_pointe)
    
    
    moy_non = sum(horraire_non_pointe) / len(horraire_non_pointe)
    variance_non_pointe = np.var(horraire_non_pointe)

    erreur_pointe = (variance_pointe/len(horraire_pointe))*1/2
    
    erreur_non_pointe = (variance_non_pointe/len(horraire_non_pointe))**(1/2)

    print(variance_pointe, variance_non_pointe)
    print(erreur_pointe, erreur_non_pointe)
    print(moy, moy_non)


    return moy, moy_non, erreur_pointe, erreur_non_pointe



def diagramme(pointe, non_pointe,
              erreur_pointe, erreur_non_pointe):
    
    plt.bar(range(2), [pointe, non_pointe], width = 0.1, color = 'red',
           yerr = [erreur_pointe, erreur_non_pointe],
            ecolor = 'black', capsize = 10)
    
    plt.xticks(range(2), ['Heure de non pointe', 'Heure de pointe'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title('Exemple d\' histogramme simple')
    
    plt.show()



horraire = traitement_heure('lyon')
diagramme(horraire[0], horraire[1], horraire[2], horraire[3])
















