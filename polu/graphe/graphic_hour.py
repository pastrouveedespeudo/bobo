"""We call data from database
we recuperate all data from one condition
and create a matplolib graph"""

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .function_graph import new

from .CONFIG import DATABASE
from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD

def visu_hour(city):
    """Here we call database for take hour"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cursor = conn.cursor()
    
    sql = ("""SELECT HEURE, nombre_particule FROM heure
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    
    rows = cursor.fetchall()
    liste = [i for i in rows]


    return liste


def treatment_hour(city):
    """We split it into list who corresponding to data"""
    
    schedule_point = []
    schedule_no_point = []

    data_hour = visu_hour(city)
    
  
    for i in data_hour:
        
        if i[0] == 'None' or i[0] == None or\
           i[1] == None or i[1] == 'None':
            pass

        elif i[0] == 'non_heure_pointe':
            schedule_no_point.append(int(i[1]))
        
        elif i[0] == 'heure_pointe':
            schedule_point.append(int(i[1]))

        print(i)
    
    data = len(schedule_point) + len(schedule_no_point)
    print(data)

    #We make an average
    try:
        moy = sum(schedule_point) / len(schedule_point)
    except:
        moy=0
        
    variance_point = np.var(schedule_point)
    
    try:
        moy_non = sum(schedule_no_point) / len(schedule_no_point)
    except:
        moy_non=0
        
    variance_no_point = np.var(schedule_no_point)

    error_point = (variance_point/len(schedule_point))**(1/2)
    
    error_no_point = (variance_no_point/len(schedule_no_point))**(1/2)

    print(moy,moy_non)
    return moy, moy_non, error_point, error_no_point, data



def diagram_hour(point, no_point,
                    error_point, error_no_point, save):
    

    """We create a graph and return it"""
    plt.bar(range(2), [point, no_point], width = 0.1, color = 'black',
           yerr = [error_point, error_no_point],
            ecolor = 'black', capsize = 10)
    
    plt.xticks(range(2), ['Heure de non pointe', 'Heure de pointe'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon l'heure")

    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')

    return nouveau

















