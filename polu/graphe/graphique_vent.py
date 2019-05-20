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
    
    sql = ("""SELECT vent, particule FROM ville
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def traitement_vent(ville):

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











a = visu('lyon')
for i in a:
    print(i)
    print('\n')
