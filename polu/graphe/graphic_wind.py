import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .function_graph import moyenne
from .function_graph import new

def visu_wind(city):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cursor = conn.cursor()
    
    sql = ("""SELECT vent, nombre_particule FROM vent
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_wind(data_wind):

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


    plt.bar(range(4), [data_very_strong, data_strong,
                       data_means, data_low],
                        width = 0.1, color = 'red',
                       yerr = [er_data_very_strong, er_data_strong,
                               er_data_means, er_data_low],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(4), ['vent tres fort', 'vent fort', 'vent moyen','vent faible'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le vent en km/h")
    
    nouveau = new()
    
    plt.savefig(nouveau)
    plt.clf()
    plt.close()
    
    shutil.move(nouveau, '/app/static/popo')
    return nouveau



























