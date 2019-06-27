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

def visu_pressure(city):
    """Here we call database for take pressure"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 
    cursor = conn.cursor()
    
    sql = ("""SELECT pression, nombre_particule FROM pression
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste

def treatment_pressure(data_pressure):
    """We split it into list who corresponding to data"""
    
    strong = [1]
    normal = []
    low = []

    for i in data_pressure:
        
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'forte':
            strong.append(int(i[1]))

        elif i[0] == 'normale':
            normal.append(int(i[1]))

        elif i[0] == 'faible':
            low.append(int(i[1]))
        print(i)

    data = len(strong) + len(normal) + len(low)
    print(data)

    #We make an average
    data_strong = moyenne(strong)
    data_low = moyenne(low)
    data_normal = moyenne(normal)


    return data_strong[0], data_low[0], data_normal[0],\
           data_strong[1], data_low[1], data_normal[1], data



def diagram_pressure(data_strong, data_low, data_normal,
              er_strong, er_low, er_normal, save):

    """We create a graph and return it"""
    plt.bar(range(3), [data_strong, data_low, data_normal],
                        width = 0.1, color = 'black',
                       yerr = [er_strong, er_low, er_normal],
                        ecolor = 'black', capsize = 10)


    plt.xticks(range(3), ['forte pression', 'faible pression',
                          'pression normale'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon la pression en hpa")
    
    nouveau = new()
    print(nouveau)
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau











