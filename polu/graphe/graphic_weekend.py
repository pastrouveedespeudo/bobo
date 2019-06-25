import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil
from .function_graph import moyenne
from .function_graph import new

def visu_weekend(city):
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')

    cursor = conn.cursor()
    
    sql = ("""SELECT WEEKEND, nombre_particule FROM weekend
            WHERE nom_ville = %s;""")
    
    values = (city)

    cursor.execute(sql, (city,))

    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_weekend(data_weekend):

    weekend = []
    no_weekend = []

    
    for i in data_weekend:
        print(i)
        if i[1] == 'None' or i[1] == None\
            or i[0] == 'None' or i[0] == None:
                pass
            
        elif i[0] == 'weekend':
            weekend.append(int(i[1]))
            
        elif i[0] == 'jour_semaine':
            no_weekend.append(int(i[1]))


    data = len(weekend) + len(no_weekend)
    print(data)
    data_weekend = moyenne(weekend)
    data_no_weekend = moyenne(no_weekend)




    return data_weekend[0], data_no_weekend[0],\
            data_weekend[1], data_no_weekend[1], data
   


def diagram_weekend(data_weekend, data_no_weekend,
              er_weekend, er_no_weekend, save):


    plt.bar(range(2), [data_weekend, data_no_weekend],
                        width = 0.1, color = 'black',
                       yerr = [er_weekend, er_no_weekend],
                        ecolor = 'black', capsize = 10)
                


    plt.xticks(range(2), ['weekd end', 'jour de semaine'])

        
    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon le weekend")
    
    nouveau = new()
    
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()
    shutil.move(nouveau, '/app/static/popo')
    return nouveau


















