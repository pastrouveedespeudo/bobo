import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .fonction_graphe import new


def visu_horraire(ville):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""SELECT HEURE, nombre_particule FROM heure
            WHERE nom_ville = %s;""")
    
    values = (ville)

    cursor.execute(sql, (ville,))

    
    rows = cursor.fetchall()
    liste = [i for i in rows]


    return liste


def traitement_heure(ville):

    horraire_pointe = []
    horraire_non_pointe = []

    donnée = visu_horraire(ville)
    
  
    for i in donnée:
        
        if i[0] == 'None' or i[0] == None or\
           i[1] == None or i[1] == 'None':
            pass

        elif i[0] == 'non_heure_pointe':
            horraire_non_pointe.append(int(i[1]))
        
        elif i[0] == 'heure_pointe':
            horraire_pointe.append(int(i[1]))

        print(i)
    
    data = len(horraire_pointe) + len(horraire_non_pointe)
    print(data)

    
    try:
        moy = sum(horraire_pointe) / len(horraire_pointe)
    except:
        moy=0
        
    variance_pointe = np.var(horraire_pointe)
    
    try:
        moy_non = sum(horraire_non_pointe) / len(horraire_non_pointe)
    except:
        moy_non=0
        
    variance_non_pointe = np.var(horraire_non_pointe)

    erreur_pointe = (variance_pointe/len(horraire_pointe))**(1/2)
    
    erreur_non_pointe = (variance_non_pointe/len(horraire_non_pointe))**(1/2)

    print(moy,moy_non)
    return moy, moy_non, erreur_pointe, erreur_non_pointe, data



def diagramme_heure(pointe, non_pointe,
                    erreur_pointe, erreur_non_pointe, save):
    

    
    plt.bar(range(2), [pointe, non_pointe], width = 0.1, color = 'red',
           yerr = [erreur_pointe, erreur_non_pointe],
            ecolor = 'black', capsize = 10)
    
    plt.xticks(range(2), ['Heure de non pointe', 'Heure de pointe'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon l'heure")

    nouveau = new()
    
    plt.savefig(nouveau)
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')

    return nouveau

















