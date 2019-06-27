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

def visu_wind(city):
    """Here we call database for take wind"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cursor = conn.cursor()
    
    sql = ("""SELECT vent, nombre_particule FROM vent
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_wind(data_wind):
    """We split it into list who corresponding to data"""
    
    very_strong = []
    strong = []
    means = []
    low = []

 
    for i in data_wind:
        print(i)
        if i[1] == 'None' or i[1] == None\
            or i[0] == 'None' or i[0] == None:
                pass
        elif i[0] == 'tres fort':
            very_strong.append(int(i[1]))
        
        elif i[0] == 'fort':
            strong.append(int(i[1]))

        elif i[0] == 'moyen fort':
            means.append(int(i[1]))

        elif i[0] == 'faible':
            low.append(int(i[1]))

    #We make an average
    data = len(very_strong) + len(strong) + len(means) + len(low)
    print(data)
    
    data_very_strong = moyenne(very_strong)
    data_strong = moyenne(strong)
    data_means = moyenne(means)
    data_low = moyenne(low)

    
    return data_very_strong[0], data_strong[0],\
           data_means[0], data_low[0],\
           data_very_strong[1], data_strong[1],\
           data_means[1], data_low[1], data


def diagram_wind(data_very_strong, data_strong, data_means, data_low,
              er_data_very_strong, er_data_strong,
                 er_data_means, er_data_low, save):

    """We create a graph and return it"""
    plt.bar(range(4), [data_very_strong, data_strong,
                       data_means, data_low],
                        width = 0.1, color = 'black',
                       yerr = [er_data_very_strong, er_data_strong,
                               er_data_means, er_data_low],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(4), ['vent tres fort', 'vent fort', 'vent moyen','vent faible'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le vent en km/h")
    
    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau



























