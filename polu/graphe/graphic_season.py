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

def visu_season(city):
    """Here we call database for take season"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cursor = conn.cursor()
    
    sql = ("""SELECT saison, nombre_particule FROM saison
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_season(data_season):
    """We split it into list who corresponding to data"""

    spring = []
    summer = []
    winter = [1]
    autumn = [1]


    for i in data_season:
        print(i)
        if i[1] == 'None' or i[1] == None\
            or i[0] == 'None' or i[0] == None:
                pass
        elif i[0] == 'primtemps':
            spring.append(int(i[1]))
        elif i[0] == 'été':
            summer.append(int(i[1]))
        elif i[0] == 'hiver':
            winter.append(int(i[1]))  
        elif i[0] == 'automne':
            autumn.append(int(i[1])) 

    #We make an average
    data = len(spring) + len(summer) + len(winter) + len(autumn)
    print(data)
    
    data_spring = moyenne(spring)
    data_summer = moyenne(summer)
    data_winter = moyenne(winter)
    data_autumn = moyenne(autumn)



    return data_spring[0], data_summer[0], data_winter[0],\
            data_autumn[0], data_spring[1], data_summer[1],\
            data_winter[1], data_autumn[1], data


def diagram_season(data_spring, data_summer, data_winter, data_autumn,
              er_sping, er_summer, er_winter, er_autumn, save):

    """We create a graph and return it"""
    plt.bar(range(4), [data_spring, data_summer, data_winter,
                       data_autumn],
                        width = 0.1, color = 'black',
                       yerr = [er_sping, er_summer, er_winter,
                              er_autumn],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(4), ['primtemps', 'été', 'hiver',
                          'automne'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les saisons")

    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau

















