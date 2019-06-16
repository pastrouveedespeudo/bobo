import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .function_graph import new
from .function_graph import *

def visu_weater(city):
    
    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    sql = ("""SELECT météo, nombre_particule FROM météo
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste



def treatement_weather(data_weather):
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

    data_good_weather = moyenne(good_weather)
    data_cloud = moyenne(cloud)
    data_rain = moyenne(rain)



    return data_good_weather[0], data_cloud[0], data_rain[0],\
           data_good_weather[1], data_cloud[1], data_rain[1], data



def diagram_weather(data_good_weather, data_cloud, data_rain,
              er_good_weather, er_cloud, er_rain, save):


    
    plt.bar(range(3), [data_good_weather, data_cloud, data_rain],
                        width = 0.1, color = 'red',
                       yerr = [er_good_weather, er_cloud, er_rain],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(3), ['beau temps', 'nuageux', 'pluie'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le temps")

    nouveau = new()

    
    plt.savefig(nouveau)
    plt.clf()
    shutil.move(nouveau, '/app/static/popo')

    return nouveau









































