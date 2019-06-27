"""We call data from database
we recuperate all data from one condition
and create a matplolib graph"""

import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .function_graph import moyenne
from .function_graph import new

from .CONFIG import DATABASE
from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD

def visu_population():
    """Here we call database for take population"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cursor = conn.cursor()
    
    cursor.execute("""SELECT POPULATION_ACTIVE_HABITANT,
                    nom_ville,
                    nombre_particule FROM conditions2;""")
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatement_population(data_population):
    """We split it into list who corresponding to data"""
    
    lyon = []
    paris = []
    marseille = []

  
    for i in data_population:
        
        if i[0] == 'None' or i[0] == None or\
           i[1] == None or i[1] == 'None'\
            or i[2] == None or i[2] == 'None':
                pass

        elif i[1] == 'lyon':
            lyon.append(int(i[2]))
        elif i[1] == 'paris':
            paris.append(int(i[2]))
        elif i[1] == 'marseille':
            marseille.append(int(i[2]))
            
        print(i)

    #We make an average
    data = len(lyon) + len(paris) + len(marseille)
    data_lyon = moyenne(lyon)
    data_paris = moyenne(paris)
    data_marseille = moyenne(marseille)



    return data_lyon[0], data_paris[0], data_marseille[0],\
            data_lyon[1], data_paris[1], data_marseille[1]
   


def diagram_population(data_lyon, data_paris, data_marseille,
              er_lyon, er_paris, er_marseille, save):

    """We create a graph and return it"""

    plt.bar(range(3), [data_lyon, data_paris, data_marseille],
                        width = 0.1, color = 'black',
                       yerr = [er_lyon, er_paris, er_marseille],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['plus de 300 K', 'plus de 1M', 'plus de 500 K'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le taux de population active")

    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    shutil.move(nouveau, '/app/static/popo')

    return nouveau
