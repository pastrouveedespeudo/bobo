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


def visu_traffic(city):
    """Here we call database for take traffic"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cursor = conn.cursor()
    
    sql = ("""SELECT TRAFIQUE, nombre_particule FROM traffique
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_traffic(data_traffic):
    """We split it into list who corresponding to data"""
    
    deaparture = []
    regular_day = []

 
    for i in data_traffic:
    
        if i[0] == None or i[0] == 'None' or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'regulier jour':
            regular_day.append(int(i[1]))
        elif i[0] == 'depart_routier':
            deaparture.append(int(i[1]))

        print(i)
        
    data = len(deaparture) + len(regular_day)
    print(data)

    #We make an average
    data_regular_day = moyenne(regular_day)
    data_deaparture = moyenne(deaparture)

    return data_regular_day[0], data_deaparture[0],\
            data_regular_day[1], data_deaparture[1], data

def diagram_traffic(data_regular_day, data_deaparture,
              er_regular_day, er_deaparture, save):

    """We create a graph and return it"""
    
    plt.bar(range(2), [data_regular_day, data_deaparture],
                        width = 0.1, color = 'black',
                       yerr = [er_regular_day, er_deaparture],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['régulier jour', 'départ routier'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les départ routiers")

    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau
























































