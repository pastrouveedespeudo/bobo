import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil


def visu_horraire(ville):
    
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

    donnée = visu_horraire(ville)


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

    erreur_pointe = (variance_pointe/len(horraire_pointe))**(1/2)
    
    erreur_non_pointe = (variance_non_pointe/len(horraire_non_pointe))**(1/2)

    print(variance_pointe, variance_non_pointe)
    print(erreur_pointe, erreur_non_pointe)
    print(moy, moy_non)


    return moy, moy_non, erreur_pointe, erreur_non_pointe



def diagramme_heure(pointe, non_pointe,
              erreur_pointe, erreur_non_pointe, save):
    
    try:
        os.remove(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo\diagramme_heure.png')
    except:
        pass
    
    plt.bar(range(2), [pointe, non_pointe], width = 0.1, color = 'red',
           yerr = [erreur_pointe, erreur_non_pointe],
            ecolor = 'black', capsize = 10)
    
    plt.xticks(range(2), ['Heure de non pointe', 'Heure de pointe'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon l'heure")
    
    plt.savefig(save)
    shutil.move(save, r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')



















