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


def visu_demonstration(city):
    """Here we call database for take demonstration"""


    conn = psycopg2.connect(database=DATABASE,
                             user=USER,
                             host=HOST,
                             password=PASSWORD)  

    cursor = conn.cursor()
    
    sql = ("""SELECT ACTIVITE_EXEPTIONNELLE, nombre_particule FROM activité
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatement_demonstration(data_demonstration):
    """We split it into list who corresponding to data"""
    
    demonstration = []
    no_demonstration = []
    
    for i in data_demonstration:
        print(i)
        if i[1] == 'None' or i[1] == None\
           or i[0] == 'None' or i[0] == None:
            pass
        elif i[0] == 'manifestation':
            demonstration.append(int(i[1]))
        elif i[0] == 'non_manifestation':
            no_demonstration.append(int(i[1]))



    data = len(demonstration) + len(no_demonstration)
    print(data)

    #We make an average
    data_demon = moyenne(demonstration)
    data_no_demon = moyenne(no_demonstration)


    return data_demon[0], data_no_demon[0],\
            data_demon[1], data_no_demon[1], data


def diagram_demonstration(data_demons, data_no_demons,
              error_demons, error_no_demons, save):

    """We create a graph and return it"""
    
    plt.bar(range(2), [data_demons, data_no_demons],
                        width = 0.1, color = 'black',
                       yerr = [error_demons, error_no_demons],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['manifestation', 'non manifestation'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les manifestation")
    
    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    shutil.move(nouveau, '/app/static/popo')
    return nouveau


























































