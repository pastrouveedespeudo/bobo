import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .function_graph import moyenne
from .function_graph import new


def visu_pressure(city):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')
    cursor = conn.cursor()
    
    sql = ("""SELECT pression, nombre_particule FROM pression
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste

def treatment_pressure(data_pressure):

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

    data_strong = moyenne(strong)
    data_low = moyenne(low)
    data_normal = moyenne(normal)


    return data_strong[0], data_low[0], data_normal[0],\
           data_strong[1], data_low[1], data_normal[1], data



def diagram_pressure(data_strong, data_low, data_normal,
              er_strong, er_low, er_normal, save):

    
    plt.bar(range(3), [data_strong, data_low, data_normal],
                        width = 0.1, color = 'red',
                       yerr = [er_strong, er_low, er_normal],
                        ecolor = 'black', capsize = 10)


    plt.xticks(range(3), ['forte pression', 'faible pression',
                          'pression normale'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon la pression en hpa")
    
    nouveau = new()
    print(nouveau)
    plt.savefig(nouveau)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau











