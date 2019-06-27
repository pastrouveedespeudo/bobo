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

from .function_graph import new
from .function_graph import *

from .CONFIG import DATABASE
from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD


def visu_weater(city):
    """Here we call database for take weather"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cursor = conn.cursor()
    
    sql = ("""SELECT météo, nombre_particule FROM météo
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste



def treatement_weather(data_weather):
    """We split it into list who corresponding to data"""
    
    good_weather = []
    cloud = []
    rain = []

 
    for i in data_weather:
        if i[0] == 'None' or i[0] == None or\
           i[1] == None or i[1] == 'None':
            pass
        elif i[0] == 'beau_temps':
            good_weather.append(int(i[1]))

        elif i[0] == 'nuageux':
            cloud.append(int(i[1]))

        elif i[0] == 'pluie':
            rain.append(int(i[1]))

        print(i)

   
    data = len(good_weather) + len(cloud) + len(rain)
    print(data)

    #We make an average
    data_good_weather = moyenne(good_weather)
    data_cloud = moyenne(cloud)
    data_rain = moyenne(rain)



    return data_good_weather[0], data_cloud[0], data_rain[0],\
           data_good_weather[1], data_cloud[1], data_rain[1], data



def diagram_weather(data_good_weather, data_cloud, data_rain,
              er_good_weather, er_cloud, er_rain, save):

    """We create a graph and return it"""
    
    plt.bar(range(3), [data_good_weather, data_cloud, data_rain],
                        width = 0.1, color = 'black',
                       yerr = [er_good_weather, er_cloud, er_rain],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['beau temps', 'nuageux', 'pluie'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le temps")

    nouveau = new()

    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    shutil.move(nouveau, '/app/static/popo')

    return nouveau









































